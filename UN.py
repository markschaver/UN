import polars as pl
import pandas as pd # Import pandas for the markdown export

# --- Data Loading and Processing (same as before) ---

# Define the file path
file_path = "/Users/markschaver/Library/CloudStorage/OneDrive-Personal/Archive/Code/UN/un-coincidence-2023.csv"

# Read the CSV file into a Polars DataFrame
try:
    un = pl.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
    # Create a dummy DataFrame to allow the rest of the script to run without error
    un = pl.DataFrame({
        "Country 1": ["USA", "France", "Russia", "China"],
        "Country 2": ["UK", "Germany", "Iran", "Pakistan"],
        "COINCIDENCE": [0.95, 0.80, 0.15, 0.50]
    })
    print("Using a dummy DataFrame for demonstration.")

# 1. Find the most similar countries
max_coincidence = un.select(pl.max("COINCIDENCE")).item()
most_similar = un.filter(pl.col("COINCIDENCE") == max_coincidence)

# 2. Find countries with high similarity (> 0.75)
closest_sorted = un.filter(pl.col("COINCIDENCE") > 0.75).sort("COINCIDENCE", descending=True)

# 3. Find the most dissimilar countries (< 0.2)
farthest_sorted = un.filter(pl.col("COINCIDENCE") < 0.2).sort("COINCIDENCE")


# --- NEW: Save all results to a Markdown file ---

output_filename = "UN-python.md"

with open(output_filename, "w") as f:
    # Write a main title for the Markdown file
    f.write("# UN Voting Coincidence Analysis\n\n")
    f.write("This report is generated from a Python script using the Polars library.\n\n")

    # Section 1: Most Similar
    f.write("## Most Similar (Max Coincidence)\n\n")
    # Convert Polars DF to Pandas DF, then to Markdown string
    markdown_table = most_similar.to_pandas().to_markdown(index=False)
    f.write(markdown_table)
    f.write("\n\n") # Add newlines for spacing in Markdown

    # Section 2: Closest
    f.write("## Closest (Coincidence > 0.75)\n\n")
    markdown_table = closest_sorted.to_pandas().to_markdown(index=False)
    f.write(markdown_table)
    f.write("\n\n")

    # Section 3: Farthest
    f.write("## Farthest (Coincidence < 0.2)\n\n")
    markdown_table = farthest_sorted.to_pandas().to_markdown(index=False)
    f.write(markdown_table)
    f.write("\n")

print(f"Successfully saved the output to {output_filename}")
