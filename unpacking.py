# [ Task 1 ]

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3)
]

# Process orders: provided a list of tuples
def process_orders(orders):

    for customer_name, product, quantity in orders:
        print(f"Customer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")

process_orders(orders)
