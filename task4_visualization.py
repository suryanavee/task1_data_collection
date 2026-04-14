import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/trends_analysed.csv")

print("Rows loaded:", len(df))


if not os.path.exists("outputs"):
    os.mkdir("outputs")
plt.savefig("outputs/file_name.png")  
plt.show()  


top10 = df.sort_values(by="score", ascending=False).head(10)

top10["short_title"] = top10["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

plt.figure()

plt.barh(top10["short_title"], top10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()  

plt.savefig("outputs/chart1_top_stories.png")

plt.show()

category_counts = df["category"].value_counts()

plt.figure()

plt.bar(category_counts.index, category_counts.values)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")

plt.show()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()


plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")


plt.legend()


plt.savefig("outputs/chart3_scatter.png")

plt.show()


category_counts = df["category"].value_counts()

top10 = df.sort_values(by="score", ascending=False).head(10)
top10["short_title"] = top10["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].barh(top10["short_title"], top10["score"])
axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].invert_yaxis()


axes[0, 1].bar(category_counts.index, category_counts.values)
axes[0, 1].set_title("Stories per Category")

axes[1, 0].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[1, 0].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[1, 0].set_title("Score vs Comments")
axes[1, 0].legend()


axes[1, 1].axis("off")

plt.suptitle("TrendPulse Dashboard")

plt.tight_layout()

plt.savefig("outputs/dashboard.png")

plt.show()
