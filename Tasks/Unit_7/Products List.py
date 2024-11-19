# products = "Milk,Cottage,Tomatoes,Milk,Cottage,Tomatoes".lower().split(",")
products = input("Enter a list of products, separated by commas: ").lower().split(",")
products_list = []

for product in products:
    products_list.append(product.strip())

while True:
    action_number = input(
        "1. Display all products\n"
        "2. Display number of products\n"
        "3. Check if a product exists\n"
        "4. Count occurrences of a product\n"
        "5. Remove a product\n"
        "6. Add a product\n"
        "7. Show invalid products (less than 3 characters or non-alphabetic)\n"
        "8. Remove duplicates\n"
        "9. Exit\n"
        "Choose an action number: "
    )

    match action_number:
        case "1":
            for item in products_list:
                print(item)
        
        case "2":
            print(len(products_list))
        
        case "3":
            print(input("Enter product name to check: ").lower() in products_list)
        
        case "4":
            print(products_list.count(input("Enter product name to count: ").lower()))
        
        case "5":
            products_list.remove(input("Enter product name to remove: ").lower())
        
        case "6":
            products_list.append(input("Enter product name to add: ").lower())
        
        case "7":
            for item in products_list:
                if len(item) < 3 or not item.isalpha():
                    print(item)
        
        case "8":
            for item in products_list:
                if products_list.count(item) > 1:
                    products_list.remove(item)
        
        case "9":
            break

        case _:
            print("Please enter a valid action number.")
