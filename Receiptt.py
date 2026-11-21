# Store Order Receipt - Amina's Stationery Store

store_name = "Amina's Stationery Store"
customer_name = "Chidi Okafor"
product_name = "A4 Notebook"
unit_price = 850.00
items_purchased = 12
total_stock = 100
delivery_fee = 500.00
payment_confirmed = True

print(customer_name)

subtotal = unit_price * items_purchased
print(subtotal)

subtotal = unit_price * items_purchased
print(subtotal)


# ----- Calculations -----
subtotal = unit_price * items_purchased
grand_total = subtotal + delivery_fee
average_cost_per_item = grand_total / items_purchased
remaining_stock = total_stock - items_purchased

# ----- Payment status -----
if payment_confirmed:
    payment_status = "Paid"
else:
    payment_status = "Pending"
print(payment_status)