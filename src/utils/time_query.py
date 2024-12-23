from datetime import datetime
import pytz


# Mapping of city names to time zones
CITY_TIMEZONE_MAPPING = {
    'kolkata': 'Asia/Kolkata',
    'shanghai': 'Asia/Shanghai',
    'new_york': 'America/New_York',
    'london': 'Europe/London',
    'tokyo': 'Asia/Tokyo',
    'sydney': 'Australia/Sydney',
    'mumbai': 'Asia/Kolkata',
    # Add more cities and their time zones as needed
}


def handle_time_query(qname):
    #Extract the city name from the query
    qname_str = str(qname).strip('.')
    parts = qname_str.split('.')
    if len(parts) < 2 or parts[-1] != 'time':
        return "Invalid query"

    city = parts[-2].replace('_', ' ').lower()
    if city == "now":
        return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    if city in CITY_TIMEZONE_MAPPING:
        timezone_str = CITY_TIMEZONE_MAPPING[city]
    try:
        timezone = pytz.timezone(timezone_str)
        current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        return f"Current time in {city}: {current_time}"
    except pytz.UnknownTimeZoneError:
        return f"Unknown city: {city}"