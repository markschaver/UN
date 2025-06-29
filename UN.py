import polars as pl

# In Python, it's more common to specify the full path directly
# rather than changing the working directory.
# If the script is in the same folder as the CSV, you can just use the filename.
file_path = "/Users/markschaver/Library/CloudStorage/OneDrive-Personal/Archive/Code/UN/un-coincidence-2023.csv"
# Or provide the full path:
# file_path = "/Users/markschaver/Library/CloudStorage/OneDrive-Personal/Archive/Code/UN/un-coincidence-2023.csv"

# Read the CSV file into a Polars DataFrame
try:
    un = pl.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
    # Create a dummy DataFrame to allow the rest of the script to run without error
    un = pl.DataFrame({
        "Country 1": ["A", "B", "C", "D"],
        "Country 2": ["B", "C", "D", "A"],
        "COINCIDENCE": [0.95, 0.80, 0.15, 0.50]
    })
    print("Using a dummy DataFrame for demonstration.")


# --- 1. Find the most similar countries ---
# R: most_similar <- filter(un, un["COINCIDENCE"] == max(un["COINCIDENCE"]))
max_coincidence = un.select(pl.max("COINCIDENCE")).item()
most_similar = un.filter(pl.col("COINCIDENCE") == max_coincidence)

# R: kable(most_similar)
# In Python, we simply print the DataFrame.
# Polars provides a clean, table-like output.
print("--- Most Similar (Max Coincidence) ---")
print(most_similar)


# --- 2. Find countries with high similarity (> 0.75) ---
# R: closest <- filter(un, un["COINCIDENCE"] > .75)
closest = un.filter(pl.col("COINCIDENCE") > 0.75)

# R: kable(arrange(closest, desc(COINCIDENCE)))
# In Polars, we chain the sort method.
closest_sorted = closest.sort("COINCIDENCE", descending=True)
print("\n--- Closest (Coincidence > 0.75, sorted) ---")
print(closest_sorted)


# --- 3. Find the most dissimilar countries (< 0.2) ---
# R: farthest <- filter(un, un["COINCIDENCE"] < .2)
farthest = un.filter(pl.col("COINCIDENCE") < 0.2)

# R: kable(arrange(farthest, COINCIDENCE))
# Sorting is ascending by default.
farthest_sorted = farthest.sort("COINCIDENCE")
print("\n--- Farthest (Coincidence < 0.2, sorted) ---")
print(farthest_sorted)

