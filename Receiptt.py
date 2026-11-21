# Store Order Receipt - Amina's Stationery Store

store_name = "Obi's Stationery Store"
customer_name = "obi john"
product_name = "A4 Notebook"
unit_price = 850.00
items_purchased = 12
total_stock = 100
delivery_fee = 500.00
payment_confirmed = True


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



# ----- Receipt -----
print("==============================")
print(store_name)
print("ORDER RECEIPT")
print("==============================")
print("Customer:", customer_name)
print("Product:", product_name)
print("Unit price:", unit_price)
print("Quantity bought:", items_purchased)
print("------------------------------")
print("Subtotal:", subtotal)
print("Delivery fee:", delivery_fee)
print("Grand total:", grand_total)
print("Average per item:", average_cost_per_item)
print("------------------------------")
print("Remaining stock:", remaining_stock)
print("Payment status:", payment_status)
print("==============================")
print("Thank you for shopping at", store_name)

