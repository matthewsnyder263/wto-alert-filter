import pandas as pd
import os
import sys
import subprocess

animal_keywords = [
    "bovine", "cattle", "cow", "beef", "pork", "swine", "porcine", "pig",
    "goat", "caprine", "sheep", "ovine", "lamb", "chicken", "poultry", "egg",
    "avian", "turkey", "duck", "animal", "meat", "milk", "dairy", "ruminant",
    "hoof", "offal", "livestock"
]
animal_keywords = [kw.lower() for kw in animal_keywords]

# Load the Excel file
file_name = "Notifications.xlsx"
try:
    df = pd.read_excel(file_name, engine="openpyxl")
except FileNotFoundError:
    print(f"ERROR: '{file_name}' not found. Make sure it's in the same folder as this script.")
    sys.exit(1)

df.columns = [col.strip() for col in df.columns]

# put my filter logic here
def row_contains_keywords(row):
    combined_text = (
        str(row.get("Title", "")) + " " +
        str(row.get("Description", "")) + " " +
        str(row.get("Products covered", ""))
    ).lower()
    return any(keyword in combined_text for keyword in animal_keywords)

filtered_df = df[df.apply(row_contains_keywords, axis=1)]

# save results and open file
output_file = "filtered_notifications.csv"
if not filtered_df.empty:
    filtered_df.to_csv(output_file, index=False)
    print(f"Filtered results saved to '{output_file}'")

    # Open the CSV file after saving
    try:
        os.startfile(output_file)  # Windows-specific
    except AttributeError:
        subprocess.call(['open', output_file])  # macOS fallback
else:
    print("No animal-related notifications found.")
