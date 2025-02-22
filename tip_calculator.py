def calculate_tip(bill, tip_percentage):
    tip = bill * (tip_percentage / 100)
    total = bill + tip
    return tip, total

if __name__ == "__main__":
    bill = float(input("Enter the bill amount: $"))
    tip_percent = float(input("Enter the tip percentage: "))
    tip_amount, total_amount = calculate_tip(bill, tip_percent)
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total: ${total_amount:.2f}")