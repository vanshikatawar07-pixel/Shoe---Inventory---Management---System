# PYTHON PROJECT : SHOE INVENTORY AND MANUFACTURING ORDER MANAGEMENT SYSTEM

# Initial shoe inventory (available stock in pairs)
inventory = {
    "Nike Sneakers": 70,
    "Adidas Sports Shoes": 45,
    "Puma Running Shoes": 80,
    "Reebok Training Shoes": 50,
    "Formal Leather Shoes": 25,
    "Sandals": 75
}

# Minimum stock level for each shoe type (in pairs)
minimum_stock = 20

# Store manufacturing orders
manufacturing_order = {}

# Shoe sale prices (in Rs)
sale_price = {
    "Nike Sneakers": 1200,
    "Adidas Sports Shoes": 800,
    "Puma Running Shoes": 1500,
    "Reebok Training Shoes": 1000,
    "Formal Leather Shoes": 2000,
    "Sandals": 500
}

# Manufacturing prices (in Rs)
manufacturing_price = {
    "Nike Sneakers": 800,
    "Adidas Sports Shoes": 450,
    "Puma Running Shoes": 1000,
    "Reebok Training Shoes": 600,
    "Formal Leather Shoes": 1200,
    "Sandals": 300
}

total_shoes_sold = 0
total_sales_amount = 0
total_manufacturing_cost = 0
total_profit = 0

# Display current inventory
for shoe, quantity  in inventory.items():
    print(f"Current stock for {shoe}: {quantity} pairs")

# Taking user input for shoe types and number of pairs sold
shoes = [x.strip() for x in input("Enter the shoe types for which you want to check stock separated by commas: ").split(",")]
sales_quantity = [int(x) for x in input("Enter the number of pairs sold for each shoe type separated by commas: ").split(",")]

# Process sales using zip
for shoe, sale in zip(shoes, sales_quantity):

    # Check for invalid sales quantity
    if sale < 0:
        print(f"Invalid sale quantity for {shoe}.")
        continue
    
    if shoe in inventory:

        # Update inventory based on sales
        if sale <= inventory[shoe]:
            inventory[shoe] -= sale

            # Update total shoes sold and total sales amount
            total_shoes_sold += sale
            total_sales_amount += sale * sale_price[shoe]
            
            # Calculate total profit for the sold shoes
            profit = sale*(sale_price[shoe] - manufacturing_price[shoe])
            total_profit += profit

        else:
            print(f"Not enough stock for {shoe}. Only {inventory[shoe]} pairs available. Sale not processed.")
            continue

        quantity = inventory[shoe]
        print(f"Remaining stock for {shoe}: {quantity} pairs")
        
        # Check if manufacturing order is needed
        if quantity < minimum_stock:
            manufacturing_order[shoe] = minimum_stock - quantity
            print(f"Manufacturing order placed for {shoe}: {manufacturing_order[shoe]} pairs")

            # Add manufactured shoes to inventory 
            inventory[shoe] += manufacturing_order[shoe]

            # Calculate total cost for the manufacturing order
            cost = manufacturing_order[shoe] * manufacturing_price[shoe]
            print(f"Total cost for manufacturing order of {shoe}: Rs{cost}")
            total_manufacturing_cost += cost
            print(f"Updated stock after manufacturing: {inventory[shoe]} pairs")

        else:
            print(f"Remaining stock for {shoe} is sufficient. No manufacturing order needed.")

    else:
        print(f"{shoe} is not available in inventory")

# Final summary 
print("\nFinal Summary")

print(f"Total shoes sold: {total_shoes_sold}")

print(f"Total sales amount: Rs {total_sales_amount}")

print(f"Total manufacturing cost: Rs {total_manufacturing_cost}")

print(f"Total profit: Rs {total_profit}")

if manufacturing_order:
    print("\nManufacturing Orders:")
    for shoe, quantity in manufacturing_order.items():
        print(f"{shoe}: {quantity} pairs")
else:
    print("\nNo manufacturing orders required.")

print("\nUpdated Inventory:")
for shoe, quantity in inventory.items():
    print(f"{shoe}: {quantity} pairs")