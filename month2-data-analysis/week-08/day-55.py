#26th September 2026

"""🐍 Python Practice — Pandas Day 1
This is your first Pandas practice, so don’t jump ahead into advanced Pandas.
Use:
import pandas as pd
Create this DataFrame:
data = {
    "video_id": ["V001", "V002", "V003", "V004", "V005", "V006"],
    "signer_id": ["S01", "S02", "S01", "S03", "S02", "S01"],
    "sign": ["HELLO", "HELP", "HELLO", "YES", "HELP", "NO"],
    "environment": ["indoor", "outdoor", "outdoor", "indoor", "indoor", "outdoor"],
    "quality": ["good", "good", "poor", "good", "poor", "good"]
}
Create:
df = pd.DataFrame(data)
Task 1 — Inspect
Print:
the DataFrame
its shape
its columns
its first few rows

Task 2 — Filter
Create a result containing only:
HELLO videos
Then create another result containing only:
poor-quality videos

Task 3 — Count
Use Pandas to determine:
number of videos per sign
number of videos per signer
number of videos per environment

Task 4 — Missing data
Run:
df.isna().sum()
Explain what the output tells you.

Task 5 — Assertions
Use at least 3 assertions to test facts about your DataFrame.
For example, you could test something you know should be true about the number of rows or columns.
Don’t copy an example blindly—design your own tests."""
 
#PYTHON ANSWERS 
import pandas as pd
# Setup Dataset
data = {
     "video_id": ["V001", "V002", "V003", "V004", "V005", "V006"],
     "signer_id": ["S01", "S02", "S01", "S03", "S02", "S01"],
     "sign": ["HELLO", "HELP", "HELLO", "YES", "HELP", "NO"],
     "environment": ["indoor", "outdoor", "outdoor", "indoor", "indoor", "outdoor"],
     "quality": ["good", "good", "poor", "good", "poor", "good"]
 }
df = pd.DataFrame(data)


# --- Task 1: Inspect ---
print("--- Full DataFrame ---")
print(df)
print("\n--- Shape ---")
print(df.shape)
print("\n--- Columns ---")
print(df.columns)
print("\n--- First Few Rows ---")
print(df.head())


# --- Task 2: Filter ---
hello_videos = df[df["sign"] == "HELLO"]
poor_quality_videos = df[df["quality"] == "poor"]
print("\n--- HELLO Videos ---")
print(hello_videos)
print("\n--- Poor Quality Videos ---")
print(poor_quality_videos)


# --- Task 3: Count ---
videos_per_sign = df["sign"].value_counts()
videos_per_signer = df["signer_id"].value_counts()
videos_per_environment = df["environment"].value_counts()
print("\n--- Videos per Sign ---")
print(videos_per_sign)
print("\n--- Videos per Signer ---")
print(videos_per_signer)
print("\n--- Videos per Environment ---")
print(videos_per_environment)


# --- Task 4: Missing Data ---
missing_counts = df.isna().sum()
print("\n--- Missing Data Count ---")
print(missing_counts)


# --- Task 5: Assertions ---
# 1. Test total number of rows in the dataset
assert len(df) == 6, f"Expected 6 rows, got {len(df)}"

# 2. Test expected total number of columns
assert df.shape[1] == 5, f"Expected 5 columns, got {df.shape[1]}"

# 3. Test that video_id values are completely unique
assert df["video_id"].is_unique, "Found duplicate video_id entries!"

# 4. Test that there are no missing values in any column
assert df.isna().sum().sum() == 0, "Dataset contains unexpected missing values!"

