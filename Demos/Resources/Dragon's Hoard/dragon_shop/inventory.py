import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "inventory.json")


def load_inventory():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_inventory(inventory):
    with open(DATA_FILE, "w") as f:
        json.dump(inventory, f, indent=4)


def display_items(inventory):
    print()
    print(f"{'Item':<22} {'Price':>8}    {'Stock':>6}")
    print("-" * 44)
    for item in inventory:
        print(f"{item['name']:<22} ${item['price']:>7.2f}    {item['stock']:>6}")
    print()


def find_item(inventory, name):
    for item in inventory:
        if item["name"].lower() == name.lower():
            return item
    return None


def restock_item(inventory, name, quantity):
    item = find_item(inventory, name)
    if item is None:
        return False
    item["stock"] += quantity
    save_inventory(inventory)
    return True
