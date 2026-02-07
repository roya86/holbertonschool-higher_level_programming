#!/usr/bin/python3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(path="products.json"):
    """Return list of products from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Expected: list of dicts
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


def read_products_csv(path="products.csv"):
    """Return list of products from a CSV file."""
    products = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]) if row.get("id") else None,
                "name": row.get("name"),
                "category": row.get("category"),
                "price": float(row["price"]) if row.get("price") else None
            })
    return products


@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    id_param = request.args.get("id", None)

    # Validate source
    if source not in ("json", "csv"):
        return render_template("product_display.html", error="Wrong source", products=[])

    # Read from chosen source
    try:
        if source == "json":
            products_list = read_products_json()
        else:
            products_list = read_products_csv()
    except (FileNotFoundError, json.JSONDecodeError, OSError, ValueError):
        # If file missing or bad format, treat as not found (simple handling)
        return render_template("product_display.html", error="Product not found", products=[])

    # Filter by id (optional)
    if id_param is not None:
        try:
            wanted_id = int(id_param)
        except ValueError:
            return render_template("product_display.html", error="Product not found", products=[])

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])
        products_list = filtered

    return render_template("product_display.html", products=products_list, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
