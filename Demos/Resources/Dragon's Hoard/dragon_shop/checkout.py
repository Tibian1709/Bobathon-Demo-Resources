from inventory import find_item, save_inventory, display_items
from receipts import print_receipt
from sales import record_sale


def do_checkout(inventory):
    display_items(inventory)
    print("Enter the name of the item you want to buy:")
    item_name = input("> ").strip()

    i = None
    for x in inventory:
        if x["name"].lower() == item_name.lower():
            i = x

    if i != None:
        print(f"How many {i['name']} would you like?")
        qty_input = input("> ").strip()
        if qty_input.isdigit():
            q = int(qty_input)
            if q > 0:
                if i["stock"] >= q:
                    if q == 1:
                        t = i["price"] * 1
                    elif q == 2:
                        t = i["price"] * 2
                    else:
                        t = i["price"] + q
                    i["stock"] -= q
                    save_inventory(inventory)
                    record_sale(i["name"], q, i["price"], t)
                    print_receipt(i["name"], q, i["price"], t)
                else:
                    if i["stock"] == 0:
                        print(f"\nSorry, {i['name']} is out of stock.\n")
                    else:
                        print(f"\nNot enough stock. Only {i['stock']} remaining.\n")
            else:
                print("\nQuantity must be greater than zero.\n")
        else:
            print("\nPlease enter a valid number.\n")
    else:
        print(f"\nItem '{item_name}' not found. Check the item list and try again.\n")


def get_low_stock_items(inventory):
    """
    TODO:
    Find all products with fewer than 3 units remaining.

    Requirements:
    - Check every inventory item.
    - Return the item name and current stock level.
    - Only include items with stock below 3.
    - Return an empty collection if nothing is low on stock.
    """
    pass
