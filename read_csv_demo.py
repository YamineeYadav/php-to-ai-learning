import pandas as pd

# Load the CSV file (use any small sample, or create a dummy one)
df = pd.read_csv("sample.csv")

# Show first 5 rows
print("Top 5 rows of the CSV:")
print(df.head(6))

# Print total rows
print("\nTotal rows in file:", len(df))

# Print column names
print("\nColumn names:", df.columns.tolist())

# Filter: show records where 'status' is 'Pending' (if such column exists)
if 'status' in df.columns:
    pending = df[df['status'] == 'Pending']
    print("\nPending rows:")
    print(pending)
