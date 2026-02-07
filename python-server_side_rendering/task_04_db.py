#!/usr/bin/python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_from_json(filename="products.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    products = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                products.append({
                    "id": int(item.get("id")) if item.get("id") is not None else None,
                    "name": item.get("name"),
                    "category": item.get("category"),
                    "price": float(item.get("price")) if item.get("price") is not None else None
                })
    return products


def read_products_from_csv(filename="products.csv"):
    products = []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]) if row.get("id") else None,
                "name": row.get("name"),
                "category": row.get("category"),
                "price": float(row["price"]) if row.get("price") else None
            })
    return products


def read_products_from_sql(db_name="products.db"):
    """Read products from SQLite database and return list of dicts."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    products = []
    for r in rows:
        products.append({
            "id": int(r[0]),
            "name": r[1],
            "category": r[2],
            "price": float(r[3])
        })
    return products


@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id")

    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html", error="Wrong source", products=[])

    # Read data from chosen source
    try:
        if source == "json":
            products_list = read_products_from_json()
        elif source == "csv":
            products_list = read_products_from_csv()
        else:
            products_list = read_products_from_sql()
    except (FileNotFoundError, json.JSONDecodeError, sqlite3.Error, OSError, ValueError):
        return render_template("product_display.html", error="Product not found", products=[])

    # Filter by id if provided
    if id_param is not None:
        try:
            wanted_id = int(id_param)
        except ValueError:
            return render_template("product_display.html", error="Product not found", products=[])

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])

        products_list = filtered

    return render_template("product_display.html", error=None, products=products_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
