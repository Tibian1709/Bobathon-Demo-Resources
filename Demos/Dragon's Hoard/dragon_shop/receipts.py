def print_receipt(name, quantity, unit_price, total):
    print()
    print("=" * 36)
    print("        DRAGON'S HOARD")
    print("=" * 36)
    print()
    line = f"{name} x{quantity}"
    print(f"{line:<28} ${total:>6.2f}")
    print()
    print(f"{'Total:':<28} ${total:>6.2f}")
    print()
    print("May your quest be successful.")
    print("=" * 36)
    print()
