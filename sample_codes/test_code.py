def calculate_total(items):
    total=0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i]["status"] == "active":
            if data[i]["price"] > 1000:
                if data[i]["quantity"] > 5:
                    result.append(data[i])
                else:
                    result.append(data[i])
            else:
                if data[i]["quantity"] > 2:
                    result.append(data[i])
    return result


def greet_user(name):
    message="Hello, "+name
    print(message)


products = [
    {"name": "Laptop", "price": 75000, "quantity": 2, "status": "active"},
    {"name": "Mouse", "price": 800, "quantity": 10, "status": "active"},
    {"name": "Keyboard", "price": 1500, "quantity": 6, "status": "active"}
]

total = calculate_total(products)
print("Total:", total)

filtered = process_data(products)
print("Filtered products:", filtered)

greet_user("Developer")