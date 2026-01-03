#!/usr/bin/python3
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in response.json()
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
