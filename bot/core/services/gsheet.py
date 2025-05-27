import asyncio
from datetime import datetime

from google.oauth2 import service_account
from googleapiclient.discovery import build


class GSheet:
    def __init__(self, creds_path: str, spreadsheet_id: str, sheet_name: str = 'Контент'):
        self.creds_path = creds_path
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.service = None

    async def authorize(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.creds_path,
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        self.service = build('sheets', 'v4', credentials=credentials, cache_discovery=False)

    async def get_verified_events(self, start_row: int = 8):
        if not self.service:
            credentials = service_account.Credentials.from_service_account_file(
                self.creds_path,
                scopes=[
                    'https://www.googleapis.com/auth/spreadsheets',
                    'https://www.googleapis.com/auth/drive'
                ]
            )
            self.service = build('sheets', 'v4', credentials=credentials, cache_discovery=False)

        range_str = f'{self.sheet_name}!A{start_row}:N'
        result = await asyncio.to_thread(
            self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_str,
                majorDimension='ROWS'
            ).execute
        )
        values = result.get('values', [])
        events = []

        for row in values:
            if len(row) < 14:
                continue

            date_str = row[0].strip()
            platform = row[3].strip() if len(row) > 3 else ''
            title = row[4].strip() if len(row) > 4 else ''
            status = row[12].strip() if len(row) > 12 else ''
            url = row[13].strip() if len(row) > 13 else ''

            if status != 'Проверено':
                continue

            try:
                datetime.strptime(date_str, '%d.%m.%Y')  # Validate format
            except ValueError:
                continue

            events.append({
                'date': date_str,
                'platform': platform,
                'title': title,
                'url': url
            })

        return events
