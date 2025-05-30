import asyncio
import json
from datetime import datetime
from typing import List, Dict

from google.oauth2 import service_account
from googleapiclient.discovery import build
from redis.asyncio import Redis


class GSheet:
    def __init__(self, creds_path: str, spreadsheet_id: str, redis: Redis):
        self.creds_path = creds_path
        self.spreadsheet_id = spreadsheet_id
        self.service = None
        self.sheets_info = [
            ("Контент", 8),
            ("Контент 2_ШАТРЫ", 6),
        ]
        self.redis = redis
        self.cache_key = "gsheet:verified_events"
        self.cache_ttl = 300

    async def authorize(self):
        if self.service:
            return
        credentials = service_account.Credentials.from_service_account_file(
            self.creds_path,
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        self.service = build('sheets', 'v4', credentials=credentials, cache_discovery=False)

    async def fetch_sheet_values(self, sheet_name: str, start_row: int) -> List[List[str]]:
        range_str = f'{sheet_name}!A{start_row}:P'
        result = await asyncio.to_thread(
            lambda: self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_str,
                majorDimension='ROWS'
            ).execute()
        )
        return result.get('values', [])

    async def get_verified_events(self, use_cache: bool = True) -> List[Dict]:
        await self.authorize()

        if use_cache:
            cached_data = await self.redis.get(self.cache_key)
            if cached_data:
                return json.loads(cached_data)

        all_events = []

        for sheet_name, start_row in self.sheets_info:
            values = await self.fetch_sheet_values(sheet_name, start_row)
            index = 0 if sheet_name == 'Контент 2_ШАТРЫ' else 1

            for row in values:
                if len(row) < 14 + index:
                    continue

                date_str = row[0].strip()
                platform = row[3 + index].strip() if len(row) > 3 + index else ''
                title = row[4 + index].strip() if len(row) > 4 + index else ''
                status = row[12 + (index + 1 if index else 0)].strip() if len(row) > 12 + index else ''
                url = row[13 + (index + 1 if index else 0)].strip() if len(row) > 13 + index else ''

                if status != 'Проверено':
                    continue

                try:
                    datetime.strptime(date_str, '%d.%m.%Y')
                except ValueError:
                    continue

                all_events.append({
                    'date': date_str,
                    'platform': platform,
                    'title': title,
                    'url': url
                })

        await self.redis.set(self.cache_key, json.dumps(all_events, ensure_ascii=False), ex=self.cache_ttl)
        return all_events
