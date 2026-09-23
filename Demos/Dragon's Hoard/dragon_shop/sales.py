_sales_log = []


def record_sale(name, quantity, unit_price, total):
    _sales_log.append({
        "name": name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    })


def get_sales():
    return list(_sales_log)


def display_sales():
    sales = get_sales()
    if not sales:
        print("\nNo sales recorded this session.\n")
        return
    print()
    print(f"{'Item':<22} {'Qty':>4}  {'Unit':>8}  {'Total':>10}")
    print("-" * 50)
    for s in sales:
        print(f"{s['name']:<22} {s['quantity']:>4}  ${s['unit_price']:>7.2f}  ${s['total']:>9.2f}")
    print()
