import requests
import time
import os
import json
import pandas as pd
import numpy as np
from datetime import datetime 

# API URL
BASE_URL = "https://hacker-news.firebaseio.com/v0"
HEADERS = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}
def get_top_ids():
  try:
      print("Fetching top stories...")
      res = requests.get(BASE_URL + "/topstories.json", headers=HEADERS, timeout=10)
      res.raise_for_status()
      data = res.json()

      print("Total IDs received:", len(data))
      return data[:500]
  except:
    print("Error fetching top stories")
    return []

def get_top_ids():
  try:
      print("Fetching top stories...")
      res = requests.get(BASE_URL + "/topstories.json", headers=HEADERS, timeout=10)
      res.raise_for_status()
      data = res.json()

      print("Total IDs received:", len(data))
      return data[:500]
  except:
    print("Error fetching top stories")
    return []

def get_story(id):
    try:
        res = requests.get(f"{BASE_URL}/item/{id}.json", headers=HEADERS)
        return res.json()
    except:
        print("Error fetching story:", id)
        return None

def get_category(title):
    title = title.lower()
    for cat in categories:
        for word in categories[cat]:
            if word in title:
                return cat
    return None

def main():
    ids = get_top_ids()

    all_data = []
    used_ids = set()

    for cat in categories:  
        print("Processing:", cat)

        count = 0

  
        for id in ids:
            if count == 25:
                break

            story = get_story(id)

            if story is None or "title" not in story:
                continue

            c = get_category(story["title"])

            if c != cat:
                continue

            if id in used_ids:
                continue

            data = {
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": cat,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", ""),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            all_data.append(data)
            used_ids.add(id)
            count += 1

    
        if count < 25:
            for id in ids:
                if count == 25:
                    break

                if id in used_ids:
                    continue

                story = get_story(id)

                if story is None or "title" not in story:
                    continue

                data = {
                    "post_id": story.get("id"),
                    "title": story.get("title"),
                    "category": cat,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", ""),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                all_data.append(data)
                used_ids.add(id)
                count += 1

        print("Collected", count, "stories")

        time.sleep(2)

    
    if not os.path.exists("data"):
        os.mkdir("data")

    filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

    with open(filename, "w") as f:
        json.dump(all_data, f, indent=4)

    print("\nTotal stories:", len(all_data))
    print("Saved to:", filename)


    
main()


