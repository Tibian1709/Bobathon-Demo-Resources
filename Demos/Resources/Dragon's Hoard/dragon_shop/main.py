import os

from inventory import load_inventory, display_items, find_item, restock_item
from checkout import do_checkout, get_low_stock_items
from sales import display_sales


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    print()
    print("====================================")
    print("          DRAGON'S HOARD")
    print("====================================")
    print("1. Buy Item")
    print("2. View Inventory")
    print("3. View Sales")
    print("4. Restock Item")
    print("5. View Low Stock")
    print("6. Exit")
    print("====================================")


def handle_restock(inventory):
    display_items(inventory)
    print("Enter the name of the item to restock:")
    name = input("> ").strip()
    item = find_item(inventory, name)
    if item is None:
        print(f"\nItem '{name}' not found.\n")
        return
    print(f"How many units would you like to add to {item['name']}?")
    qty_input = input("> ").strip()
    if not qty_input.isdigit() or int(qty_input) <= 0:
        print("\nPlease enter a positive whole number.\n")
        return
    restock_item(inventory, name, int(qty_input))
    print(f"\n{item['name']} restocked. New stock: {item['stock']}\n")


def handle_low_stock(inventory):
    results = get_low_stock_items(inventory)
    if results is None or len(results) == 0:
        print("\nAll items are well stocked.\n")
    else:
        print()
        print(f"{'Item':<22} {'Stock':>6}")
        print("-" * 30)
        for entry in results:
            print(f"{entry['name']:<22} {entry['stock']:>6}")
        print()


def main():
    inventory = load_inventory()

    while True:
        clear()
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            do_checkout(inventory)
        elif choice == "2":
            display_items(inventory)
        elif choice == "3":
            display_sales()
        elif choice == "4":
            handle_restock(inventory)
        elif choice == "5":
            handle_low_stock(inventory)
        elif choice == "6":
            print("\nFarewell, adventurer.\n")
            break
        else:
            print("\nInvalid option. Please choose 1-6.\n")
            continue

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
