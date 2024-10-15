#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints the status code and titles of the posts."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    structured_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in data]

    with open('posts.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(structured_data)
