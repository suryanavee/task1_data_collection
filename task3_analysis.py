import pandas as pd
import numpy as np

file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nShape of DataFrame:", df.shape)

avg_score = df["score"].mean()
print("\nAverage score:", avg_score)

avg_comments = df["num_comments"].mean()
print("Average num_comments:", avg_comments)


scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

print("Score Mean:", np.mean(scores))
print("Score Median:", np.median(scores))
print("Score Std Dev:", np.std(scores))

print("\nHighest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))


top_category = df["category"].value_counts().idxmax()
print("\nCategory with most stories:", top_category)

max_comments_index = np.argmax(comments)
top_story = df.iloc[max_comments_index]

print("\nMost commented story:")
print("Title:", top_story["title"])
print("Comments:", top_story["num_comments"])

avg_score = df["score"].mean()

df["engagement"] = df["num_comments"] / (df["score"] + 1)


df["is_popular"] = df["score"] > avg_score

#print(df.head())

output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print("Saved file to:", output_file)
print("Total rows:", len(df))
