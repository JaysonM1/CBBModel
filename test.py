from datetime import datetime

# Get the current date
current_date = datetime.now()

# Format the date as 'YYYYMMDD'
formatted_date = current_date.strftime('%Y%m%d')

# Print the formatted date
print("Current date in YYYYMMDD format:", formatted_date)