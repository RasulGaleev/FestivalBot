import asyncio
from datetime import datetime
from typing import List, Dict

from google.oauth2 import service_account
from googleapiclient.discovery import build


class GSheet:
    def __init__(self, creds_path: str, spreadsheet_id: str):
        self.creds_path = creds_path
        self.spreadsheet_id = spreadsheet_id
        self.service = None
        self.sheets_info = [
            ("Контент", 8),
            ("Контент 2_ШАТРЫ", 6),
        ]

    async def authorize(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.creds_path,
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        self.service = build('sheets', 'v4', credentials=credentials, cache_discovery=False)

    async def get_verified_events(self) -> List[Dict]:
        all_events = []

        for sheet_name, start_row in self.sheets_info:
            range_str = f'{sheet_name}!A{start_row}:O'
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_str,
                majorDimension='ROWS'
            ).execute()
            index = 0 if sheet_name == 'Контент 2_ШАТРЫ' else 1
            values = result.get('values', [])
            for row in values:
                date_str = row[0].strip()
                platform = row[3 + index].strip() if len(row) > 3 + index else ''
                title = row[4 + index].strip() if len(row) > 4 + index else ''
                status = row[12 + index].strip() if len(row) > 12 + index else ''
                url = row[13 + index].strip() if len(row) > 13 + index else ''

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

        return all_events
