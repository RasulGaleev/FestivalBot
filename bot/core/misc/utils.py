from datetime import datetime
from typing import List, Dict


def get_unique_dates(events: List[Dict]) -> List[str]:
    dates = {event['date'] for event in events}
    sorted_dates = sorted(dates, key=lambda d: datetime.strptime(d, '%d.%m.%Y'))
    return sorted_dates


def get_unique_platforms(events: List[Dict]) -> List[Dict[str, str | int]]:
    locations = {event['platform'] for event in events if event.get('platform')}
    sorted_locations = sorted(locations)
    return sorted_locations


def get_events_by_date(events: List[Dict], target_date: str) -> List[Dict]:
    return [event for event in events if event['date'] == target_date]


def get_events_by_platform(events: List[Dict], platform: str) -> List[Dict]:
    return [event for event in events if event['platform'] == platform]
