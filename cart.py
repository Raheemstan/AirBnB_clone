class ShoppingCart:
    """Represents a shopping cart."""

    def __init__(self):
        self.items = []

    def add_item(self, item_name, price):
        """Add an item to the cart."""
        self.items.append({"item": item_name, "price": price})

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        total = sum(item["price"] for item in self.items)
        return total


if __name__ == "__main__":
    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item("Product 1", 10.99)
    cart.add_item("Product 2", 5.49)
    cart.add_item("Product 3", 8.75)

    # Calculate and print the total price
    total_price = cart.calculate_total()
    print(f"Total price of items in the cart: ${total_price:.2f}")
