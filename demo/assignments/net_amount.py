# Calculate amount based on qty and price

price = int(input("Enter price :"))
qty = int(input("Enter qty  :"))

amount = qty * price
discount = amount * 0.10
net_amount = amount - discount

print(f"Amount        {amount:8.2f}")
print(f" - Discount   {discount:8.2f}")
print(f"Net Amount    {net_amount:8.2f}")