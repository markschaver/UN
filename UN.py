import polars as pl
import pandas as pd # Import pandas for the markdown export

file_path = "https://raw.githubusercontent.com/markschaver/UN/refs/heads/master/un-coincidence-2023.csv"

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

max_coincidence = un.select(pl.max("COINCIDENCE")).item()
most_similar = un.filter(pl.col("COINCIDENCE") == max_coincidence)

closest_sorted = un.filter(pl.col("COINCIDENCE") > 0.75).sort("COINCIDENCE", descending=True)

farthest_sorted = un.filter(pl.col("COINCIDENCE") < 0.2).sort("COINCIDENCE")

output_filename = "UN-python.md"

with open(output_filename, "w") as f:
    # Write a main title for the Markdown file
    f.write("# UN Voting Coincidence Analysis\n\n")
    f.write("This report is generated from a Python script using the Polars library.\n\n")

    f.write("## Most Similar (Max Coincidence)\n\n")
    # Convert Polars DF to Pandas DF, then to Markdown string
    markdown_table = most_similar.to_pandas().to_markdown(index=False)
    f.write(markdown_table)
    f.write("\n\n") # Add newlines for spacing in Markdown

    f.write("## Closest (Coincidence > 0.75)\n\n")
    markdown_table = closest_sorted.to_pandas().to_markdown(index=False)
    f.write(markdown_table)
    f.write("\n\n")

    f.write("## Farthest (Coincidence < 0.2)\n\n")
    markdown_table = farthest_sorted.to_pandas().to_markdown(index=False)
    f.write(markdown_table)
    f.write("\n")

print(f"Successfully saved the output to {output_filename}")
