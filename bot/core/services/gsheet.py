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

    async def get_column_values(self, column: str, start_row: int = 1):
        range_str = f"{self.sheet_name}!{column}{start_row}:{column}"
        result = await asyncio.to_thread(
            self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_str,
                majorDimension='COLUMNS'
            ).execute
        )
        return result.get('values', [])

    async def get_date_list(self, start_row: int = 8):
        range_str = f'{self.sheet_name}!A{start_row}:M'
        result = await asyncio.to_thread(
            self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_str,
                majorDimension='ROWS'
            ).execute
        )
        values = result.get('values', [])
        parsed_dates = []

        for row in values:
            if len(row) < 13:
                continue

            date_str = row[0].strip()
            status = row[12].strip()

            if status != 'Проверено':
                continue

            try:
                parsed_date = datetime.strptime(date_str, '%d.%m.%Y')
                parsed_dates.append(parsed_date)
            except ValueError:
                continue

        unique_dates = sorted(set(parsed_dates))
        return [dt.strftime('%d.%m.%Y') for dt in unique_dates]

    async def get_title_by_date(self, date: str, start_row: int = 8):
        range_str = f'{self.sheet_name}!A{start_row}:M'
        result = await asyncio.to_thread(
            self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_str,
                majorDimension='ROWS'
            ).execute
        )
        values = result.get('values', [])
        titles = []

        for row in values:
            if len(row) < 13:
                continue

            date_str = row[0].strip()
            status = row[12].strip()

            if date_str != date or status != 'Проверено':
                continue

            title = row[4].strip() if len(row) >= 5 else ''
            titles.append(title)

        return titles
