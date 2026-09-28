# ==========================================
#       VENDING MACHINE PROJECT
# ==========================================

# Product details
products = {
    1: ["Kingfisher", 120],
    2: ["Budweiser", 180],
    3: ["Heineken", 200],
    4: ["Corona", 250]
}

# Stores completed transactions
transactions = []


# ==========================================
# 1. DISPLAY PRODUCTS
# ==========================================

def display_products():

    print("\n========== PRODUCTS ==========")

    for number, details in products.items():

        name = details[0]
        price = details[1]

        print(number, ".", name, "- ₹", price)

    print("==============================")


# ==========================================
# 2. AGE VERIFICATION
# ==========================================

def age_verification():

    age = int(input("\nEnter your age: "))

    if age >= 21:
        print("Age verification successful.")
        return True

    else:
        print("Age requirement not met.")
        return False


# ==========================================
# 3. SELECT PRODUCT
# ==========================================

def select_product():

    choice = int(input("Enter product number: "))

    if choice in products:
        return choice

    else:
        print("Invalid product number.")
        return None


# ==========================================
# 4. ADD PRODUCTS TO CART
# ==========================================

def add_to_cart(cart):

    while True:

        display_products()

        choice = select_product()

        if choice is not None:

            cart.append(choice)

            name = products[choice][0]

            print(name, "added to cart.")

        again = input(
            "\nDo you want to add another product? (yes/no): "
        ).lower()

        if again != "yes":
            break


# ==========================================
# 5. DISPLAY CART
# ==========================================

def display_cart(cart):

    print("\n========== YOUR CART ==========")

    if len(cart) == 0:

        print("Cart is empty.")
        return

    for choice in cart:

        name = products[choice][0]
        price = products[choice][1]

        print(name, "- ₹", price)

    print("===============================")


# ==========================================
# 6. CALCULATE TOTAL
# ==========================================

def calculate_total(cart):

    total = 0

    for choice in cart:

        price = products[choice][1]

        total = total + price

    return total


# ==========================================
# 7. PAYMENT
# ==========================================

def make_payment(total):

    print("\nTotal amount: ₹", total)

    while True:

        money = int(input("Enter payment: ₹"))

        if money >= total:

            change = money - total

            return money, change

        else:

            print("Insufficient payment.")

            print(
                "You need ₹",
                total - money,
                "more."
            )


# ==========================================
# 8. SAVE TRANSACTION
# ==========================================

def save_transaction(cart, total, money, change):

    transaction = {
        "items": cart.copy(),
        "total": total,
        "paid": money,
        "change": change
    }

    transactions.append(transaction)


# ==========================================
# 9. TRANSACTION HISTORY
# ==========================================

def transaction_history():

    print("\n========== TRANSACTION HISTORY ==========")

    if len(transactions) == 0:

        print("No transactions available.")

        return

    transaction_number = 1

    for transaction in transactions:

        print("\nTransaction", transaction_number)

        print("------------------------------")

        print("Items:")

        for choice in transaction["items"]:

            name = products[choice][0]
            price = products[choice][1]

            print(name, "- ₹", price)

        print("Total  : ₹", transaction["total"])
        print("Paid   : ₹", transaction["paid"])
        print("Change : ₹", transaction["change"])

        transaction_number += 1

    print("==========================================")


# ==========================================
# 10. MAIN VENDING MACHINE
# ==========================================

def vending_machine():

    print("\n====================================")
    print("       SMART VENDING MACHINE")
    print("====================================")

    # Age verification
    if not age_verification():

        print("\nAccess denied.")

        return

    while True:

        print("\n========== MAIN MENU ==========")

        print("1. Buy Products")
        print("2. View Transaction History")
        print("3. Exit")

        choice = int(input("\nEnter your choice: "))

        # ==================================
        # BUY PRODUCTS
        # ==================================

        if choice == 1:

            # Empty cart for every new order
            cart = []

            add_to_cart(cart)

            # Check whether anything was selected
            if len(cart) == 0:

                print("\nNo products selected.")

                continue

            # Show cart
            display_cart(cart)

            # Calculate total
            total = calculate_total(cart)

            # Payment
            money, change = make_payment(total)

            # Payment successful
            print("\n========== PAYMENT ==========")

            print("Total  : ₹", total)
            print("Paid   : ₹", money)
            print("Change : ₹", change)

            print("=============================")

            # Save transaction
            save_transaction(
                cart,
                total,
                money,
                change
            )

            print("\nTransaction completed successfully!")

        # ==================================
        # TRANSACTION HISTORY
        # ==================================

        elif choice == 2:

            transaction_history()

        # ==================================
        # EXIT
        # ==================================

        elif choice == 3:

            print("\nThank you for using the vending machine!")

            break

        # ==================================
        # INVALID MAIN MENU CHOICE
        # ==================================

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================
# START PROGRAM
# ==========================================

vending_machine()
