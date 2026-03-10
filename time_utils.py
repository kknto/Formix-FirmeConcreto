import os
from datetime import datetime
from zoneinfo import ZoneInfo


DEFAULT_TIMEZONE = "America/Cancun"
APP_TIMEZONE = (os.getenv("APP_TIMEZONE") or os.getenv("TZ") or DEFAULT_TIMEZONE).strip() or DEFAULT_TIMEZONE

try:
    APP_TZ = ZoneInfo(APP_TIMEZONE)
except Exception:
    APP_TZ = ZoneInfo("UTC")


def now_dt() -> datetime:
    # Return a naive datetime already shifted to the configured app timezone.
    return datetime.now(APP_TZ).replace(tzinfo=None)


def now_str() -> str:
    return now_dt().strftime("%Y-%m-%d %H:%M:%S")


def today_str() -> str:
    return now_dt().strftime("%Y-%m-%d")


def now_timestamp() -> int:
    return int(datetime.now(APP_TZ).timestamp())

