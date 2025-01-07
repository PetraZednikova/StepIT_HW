from models.pizza import Pizza
from models.topping import Topping
from models.order import Order
from models.sales import Sales
from models.payment import Payment, CreditCardPayment, PayPalPayment

class MainController:
    def __init__(self):
        self.sales = Sales()
        self.order = None
        self.menu = self.create_pizza_menu()
        self.toppings_menu = self.create_toppings_menu()

    def create_pizza_menu(self):
        return [
            Pizza("Margherita", "M", 8.0),
            Pizza("Pepperoni", "M", 10.0),
            Pizza("Hawaiian", "M", 12.0),
            Pizza("Vegetarian", "M", 9.5),
            Pizza("BBQ Chicken", "M", 13.0),
        ]

    def create_toppings_menu(self):
        return [
            Topping("Extra Cheese", 1.5),
            Topping("Mushrooms", 1.0),
            Topping("Onions", 0.5),
            Topping("Olives", 1.2),
            Topping("Bacon", 2.0),
        ]

    def run(self):
        while True:
            print("Welcome to Pizza App")
            print("1. Create Order")
            print("2. View Order")
            print("3. Payment")
            print("4. Admin Menu")
            print("5. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.create_order()
            elif choice == "2":
                self.view_order()
            elif choice == "3":
                self.process_payment()
            elif choice == "4":
                self.admin_menu()
            elif choice == "5":
                break

    def create_order(self):
        print("\nChoose a pizza from the menu:")
        self.display_menu()

        try:
            pizza_choice = int(input("Enter the number of your pizza choice: ")) - 1

            if 0 <= pizza_choice < len(self.menu):
                selected_pizza = self.menu[pizza_choice]
                print(f"You selected: {selected_pizza.name}")

                # Choose size
                print("\nSelect size:")
                print("1. Small")
                print("2. Medium")
                print("3. Large")

                size_choice = int(input("Enter the number for the size: "))
                if size_choice == 1:
                    selected_pizza.size = "S"
                    selected_pizza.base_price -= 2.0
                elif size_choice == 2:
                    selected_pizza.size = "M"
                    # Base price remains unchanged
                elif size_choice == 3:
                    selected_pizza.size = "L"
                    selected_pizza.base_price += 3.0
                else:
                    print("Invalid size choice. Defaulting to Medium.")

                print(f"You selected: {selected_pizza.name} ({selected_pizza.size}) - {selected_pizza.base_price} USD")

                # Adding toppings
                while True:
                    print("\nAvailable toppings:")
                    for idx, topping in enumerate(self.toppings_menu, 1):
                        print(f"{idx}. {topping.name} - {topping.price} USD")
                    print("0. Finish adding toppings")

                    try:
                        topping_choice = int(input("Choose a topping (or 0 to finish): "))
                        if topping_choice == 0:
                            break
                        elif 1 <= topping_choice <= len(self.toppings_menu):
                            selected_topping = self.toppings_menu[topping_choice - 1]
                            selected_pizza.add_topping(selected_topping)
                            print(f"Added: {selected_topping.name}")
                        else:
                            print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Please enter a valid number.")

                # Add pizza to order
                if not self.order:
                    self.order = Order()
                self.order.add_pizza(selected_pizza)
                print(f"\nAdded {selected_pizza.name} to your order!")
            else:
                print("Invalid pizza choice. Please select a valid number from the menu.")
        except ValueError:
            print("Please enter a valid number.")

    def display_menu(self):
        print("\nPizza Menu:")
        for idx, pizza in enumerate(self.menu, 1):
            print(f"{idx}. {pizza.name} ({pizza.size}) - {pizza.base_price} USD")

    def view_order(self):
        if not self.order or not self.order.pizzas:
            print("Your order is empty.")
        else:
            print("\nYour order:")
            for pizza in self.order.pizzas:
                print(pizza)
            print(f"Total: {self.order.calculate_total()} USD")

    def process_payment(self):
        if not self.order:
            print("No order to process.")
            return

        total = self.order.calculate_total()
        print(f"Total amount: {total}")
        print("Select Payment Method:")
        print("1. Credit Card")
        print("2. PayPal")

        choice = input("Enter payment method: ")
        if choice == "1":
            strategy = CreditCardPayment()
        elif choice == "2":
            strategy = PayPalPayment()
        else:
            print("Invalid choice.")
            return

        payment = Payment(strategy)
        payment.pay(total)
        self.sales.record_sale(self.order)
        print("Payment successful.")
        self.order = None

    def admin_menu(self):
        password = input("Enter admin password: ")
        if password == "admin":
            report = self.sales.get_sales_report()
            print("Sales Report:")
            print(f"Total Sales: {report['total_sales']} USD")
            print(f"Number of Orders: {report['orders_count']}")
        else:
            print("Incorrect password.")
