# Date and Time Practice

from datetime import datetime, timedelta, timezone

# 1. Current Date and Time
now = datetime.now()
print("Current datetime:", now)

# 2. Create Specific Date
date_obj = datetime(2026, 1, 1)
print("Specific date:", date_obj)

# 3. Date Formatting
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 4. Time Difference
future = now + timedelta(days=10)
difference = future - now
print("Difference in days:", difference.days)

# 5. Working with Timezones
utc_now = datetime.now(timezone.utc)
print("UTC time:", utc_now)
