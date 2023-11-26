import os
from datetime import datetime

# Specify the directory containing the CSV files
directory = './Scores/'

# List all files in the directory
files = os.listdir(directory)

# Loop through each file in the directory
for file in files:
    if file.endswith('.csv'):
        # Extract the date from the file name
        date_str = file.split('.')[0]

        # Convert the date to the desired format
        original_date = datetime.strptime(date_str, '%m-%d-%Y')
        new_date_str = original_date.strftime('%m-%d-%y')

        # Create the new file name
        new_file_name = f'{new_date_str}.csv'

        # Construct the full paths for the old and new file names
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

print("Files renamed successfully.")

