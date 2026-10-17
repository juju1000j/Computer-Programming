# Julien Clark
# Project 1
# Option 1

# Starting budget for customer
budgetInDollars = 100

# This is a dictionary list. It uses the dictionary type to store complicated data
menuItems = [
    {"name": "Breakfast Burrito", "Base Price": 4.50, "taxable": False},
    {"name": "Cheeseburger", "Base Price": 4.00, "taxable": False},
    {"name": "Hot Dog", "Base Price": 3.00, "taxable": False},
    {"name": "Teriyaki Bowl", "Base Price": 5.00, "taxable": False},
    {"name": "Chips", "Base Price": 1.00, "taxable": True},
    {"name": "Fries", "Base Price": 2.50, "taxable": True},
    {"name": "Soda", "Base Price": 1.75, "taxable": True},
    {"name": "Water", "Base Price": 1.50, "taxable": True},
]

# Track quantities of ordered items
order_counts = {}

while True:
    print("\n--- Menu ---")
    for index, item in enumerate(menuItems, start=1):
        print(f"{index}. {item['name']} - ${item['Base Price']:.2f} (Taxable: {item['taxable']})")

    order = input("What would you like to order from Z's today? Enter item number or name (Type 'Y' when finished): ").strip()

    if order.upper() == "Y":
        break

    # Find the selected item based on number or name
    selected_item = None
    if order.isdigit():
        idx = int(order) - 1
        if 0 <= idx < len(menuItems):
            selected_item = menuItems[idx]
    else:
        for item in menuItems:
            if item["name"].lower() == order.lower():
                selected_item = item
                break

    if selected_item:
        name = selected_item["name"]
        order_counts[name] = order_counts.get(name, 0) + 1
        print(f"-> Added {name} to your order.")
    else:
        print("Invalid choice. Please try again.")

# --- OUTPUT SUMMARY ---
print("\n" + "="*50)
print(f"{'Item':<20} {'Quantity':<10} {'Base Amount':<12} {'Total Amount'}")
print("-" * 50)

total_base_cost = 0.0
total_final_cost = 0.0

for item in menuItems:
    name = item["name"]
    if name in order_counts:
        qty = order_counts[name]
        base_price = item["Base Price"]
        base_amount = base_price * qty
        
        # Apply 10% tax if taxable is True
        if item["taxable"]:
            total_amount = base_amount * 1.10
        else:
            total_amount = base_amount
            
        total_base_cost += base_amount
        total_final_cost += total_amount
        
        print(f"{name:<20} {qty:<10} ${base_amount:<11.2f} ${total_amount:.2f}")

print("-" * 50)
print(f"{'TOTAL':<20} {'':<10} ${total_base_cost:<11.2f} ${total_final_cost:.2f}")
print("=" * 50)

# --- PAYMENT PROCESS ---
payment_type = input("What type of payment are you using? (Enter 'Cash' or 'Cub Cash'): ").strip().title()

if payment_type == "Cash":
    cash_tendered = float(input("Enter the cash handed to the employee: $"))
    change = cash_tendered - total_final_cost
    print(f"Change returned: ${change:.2f}")
    print("Thank you!")

elif payment_type == "Cub Cash":
    remaining_balance = budgetInDollars - total_final_cost
    print("Thank you for using Cub Cash!")
    print(f"Remaining card balance: ${remaining_balance:.2f}")

else:
    print("Invalid payment type selected.")