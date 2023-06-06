from datetime import datetime, timedelta


def hours_to_seconds(hours) -> int:
    return int(hours * 60 * 60)


def minutes_to_seconds(minutes) -> int:
    return int(minutes * 60)


def seconds_to_hours(seconds) -> float:
    return seconds / 60 / 60

def seconds_to_time(seconds):
    """Converts seconds past midnight to a time string."""
    return (datetime(2000, 1, 1) + timedelta(seconds=seconds)).time()

def seconds_to_hours_minutes(seconds) -> (int, int):
    return int(seconds_to_hours(seconds)), int(seconds % 3600 / 60)
