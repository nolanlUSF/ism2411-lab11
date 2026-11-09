# In the real world, you would use .get() if you are checking whether a customer provdied a phone number or not. For bracket notation, you would use it when getting a product's name.
# This pattern is just like a PivotTable in excel. Python is more useful for large datasets since you can do lots of records withouth making summaries for each, and you can run the code every day or as much as you want.

print("Excercise 1") 
customer = {
    "name": "Alice Johnson",
    "email": "alice@email.com",
    "tier": "Gold",
    "ytd_spend": 4250.75
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2
# print("Exercise 2")
# customer["phone"] = "813-555-0142"

# print(customer)
# customer["tier"] = "platinum"

# print(customer)
# del customer["email"]

# print(customer)

# print(customer.get("email", "Email not found"))

# Exercise 3

# print(customer.get("email," "no email on file"))


# try:
#     print(customer["email"])
# except KeyError as error:
#     print(f"KeyError Caught: {error}")

# exercise 4
# print("exercise 4")
# for key, value in customer.items():
#     print(f"Key {key} : {value}")

# for item in customer:
#     print(item)

# exercise 5
print("exercise 5")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.10,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}") # platinum
print(f"Discount: {discount_rate * 100:.0f}%") # 15%
print(f"Final price: ${final_price:.2f}") # $170.00

# exercise 6
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate # assuming a purchase of $300 for each customer
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")


print("Exercise 7")
catalog = {
    "widget A": {"price": 9.99, "stock": 150},
    "gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("exercise 8")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}): {sales_by_region[region]}")