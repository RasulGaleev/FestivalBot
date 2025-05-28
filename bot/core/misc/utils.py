from datetime import datetime
from typing import List, Dict, Optional


def get_unique_platforms(events: List[Dict]) -> List[Dict[str, str | int]]:
    locations = {event['platform'] for event in events if event.get('platform')}
    sorted_locations = sorted(locations)
    return sorted_locations


def get_unique_dates(events: List[Dict], platform: Optional[str] = None) -> List[str]:
    filtered_events = ([event for event in events if event.get('platform') == platform] if platform else events)
    dates = {event['date'] for event in filtered_events}
    sorted_dates = sorted(dates, key=lambda d: datetime.strptime(d, '%d.%m.%Y'))
    return sorted_dates


def get_filtered_events(events: List[Dict], date: str, platform: Optional[str] = None) -> List[Dict]:
    return [event for event in events if event['date'] == date and (
            platform is None or event.get('platform') == platform)]
