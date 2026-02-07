#!/usr/bin/python3
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    items_list = []

    try:
        with open("items.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict) and isinstance(data.get("items"), list):
                items_list = data["items"]
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
