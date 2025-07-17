# Input: Face Wash Product data
product_id = int(input("Enter product ID:"))
product_name = input("Enter product name:")
price = float(input("Enter product price(₹):"))
categories = input("Enter product categories(comma-separated):").split(",")
available_product= int(input("Enter available product:"))
sold_count= int(input("Enter sold count:"))
stock_details= (available_product,sold_count)
discount_percentage= float(map(input("Enter Discount percentage:")))
features= set(input("enter unique Features(comma-separated):").split(","))
supplier_name=input("Enter provider Name:")
supplier_contact = input("Enter Provider contact Number:")
supplier_location = input("Enter provider Location:")

supplier_details={
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

#Displaying the product details using different formatting ethods.

print("=== product Information ===")
print("product Id",product_id)
print("Name", product_name)
print("product price:",price)
print("product Discount: %.0f%% % discount_percentage")
print(f"product model Name:{product_name}")
print(f"product price per day:₹{price}")
print(f"Discount Offered:{discount_percentage}%")
print(f"Available_product:{stock_details[0]} units")
print(f"sold_count: {stock_details[1]} units")
print("supplier Details: Name -{}, contact - {}, Location - {}".format( supplier_details['Name'], supplier_details['contact'],supplier_details["location"]))
print("\ncategories:", categories)
print("Features:", features)
