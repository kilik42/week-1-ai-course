
# Import the pandas library, which is used for data manipulation
import pandas as pd

# Read the CSV file named "orders.csv" and store it as a DataFrame called df
df = pd.read_csv("orders.csv")

# Display the names of all columns in the DataFrame
# This helps us understand the structure of the dataset
df.columns

# Access the value in the "Shipped" column for the 11th row
# iloc[10] selects the row with index 10 (Python indexing starts at 0)
df.iloc[10]["Shipped"]

# Display the first 5 rows of the DataFrame
# Useful for quickly previewing the dataset
df.head()

# Filter rows where:
# Category is "Electronics" AND Country is "USA"
# Both conditions must be true for a row to be selected
df[(df["Category"] == "Electronics") & (df["Country"] == "USA")]

# Filter rows where:
# Category is "Electronics" OR Country is "USA"
# At least one of the conditions must be true
df[(df["Category"] == "Electronics") | (df["Country"] == "USA")]

# Select rows where Quantity is NOT equal to 2
# The != operator means "not equal to"
df[df["Quantity"] != 2]

# Select rows where Country is NOT one of the listed countries
# isin() checks membership, and ~ negates the condition
df[~df["Country"].isin(["USA", "Sweden", "Brazil"])]

# Replace the value "USA" with "United States" in the Country column
# This change is applied only where the condition is true
df.loc[df["Country"] == "USA", "Country"] = "United States"

# Convert all values in the Country column to uppercase
# This helps standardize text data
df["Country"] = df["Country"].str.upper()

# Rename the column "OrderID" to "Order ID"
# inplace=True applies the change directly to the DataFrame
df.rename(columns={"OrderID": "Order ID"}, inplace=True)

# Display the full DataFrame to verify all transformations
df

# Sort the DataFrame by the Price column in descending order
# Highest priced orders appear first
# Note: This does NOT permanently modify df unless reassigned
df.sort_values("Price", ascending=False)

# Save the final DataFrame to a new CSV file
# index=False prevents row numbers from being written to the file
df.to_csv("new_file.csv", index=False)

