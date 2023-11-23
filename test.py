import pandas as pd

# Load DataFrame from CSV file
input_csv_path = 'TeamAvgs\DailyStats\TeamAverages/bare.csv'
df = pd.read_csv(input_csv_path)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Drop duplicate rows based on all columns
df_no_duplicates = df.drop_duplicates(subset=['Team'])

# Display the DataFrame after dropping duplicates
print("\nDataFrame after dropping duplicates:")
print(df_no_duplicates)

# Save the modified DataFrame to a new CSV file
output_csv_path = 'your_output_file.csv'
df_no_duplicates.to_csv(output_csv_path, index=False)