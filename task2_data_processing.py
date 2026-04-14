import pandas as pd
import os

file_path = "data/trends_20260414.json"

df = pd.read_json(file_path)

print("Total rows loaded:", len(df))
#print(df.head())
#print(df.info())
print(df.isnull().sum())
print(len(df))
print("Rows after cleaning:", len(df))
df = df.drop_duplicates(subset=["post_id"])
print("After removing duplicates:", len(df))
df = df.drop_duplicates(subset=["post_id"])
print("After removing duplicates:", len(df))
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))
df["title"] = df["title"].str.strip()

print("Rows after cleaning:", len(df))


if not os.path.exists("data"):
    os.mkdir("data")
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)
print("Saved", len(df), "rows to", output_file)
print("\nStories per category:")

counts = df["category"].value_counts()

for cat, count in counts.items():
    print(cat, ":", count)
