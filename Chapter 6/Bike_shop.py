class Bicycle:
    """Models a bicycle with model, weight, and cost."""
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def __repr__(self):
        """Return string representation of Bicycle object.

        Includes the name of the class (Bicycle), the model, the weight, and the cost
        """
        return "{model}, {weight}, {cost}".format(model=self.model, weight=self.weight, cost=self.cost)


class Shop:
    """Models a bike shop.
    
    Creates and shows the bike inventory, calculates profit, and removes bikes from inventory when sold.
    """
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        # self.avail_inventory = []
        self.markup = 0.2
        self.sale_profit = 0
        self.sel_bike_price = None
        self.store_profit = 0

    def initial_inventory(self, bicycle, quantity):
        """Creates initial inventory of shop inventory"""
        self.inventory[bicycle] = quantity

    def update_inventory(self, bicycle):
        """Allows adding new bikes to inventory (Not implemented)"""
        self.inventory[bicycle] += 1

    def show_inventory(self):
        """Displays bikes currently available"""
        avail_inventory = []
        for bicycle in self.inventory:
            if self.inventory[bicycle] > 0:
                avail_inventory.append(bicycle)
        return avail_inventory

    def indiv_sale_profit(self, bike_cost):
        """Calculate how much profit the store made on a sale"""
        self.sel_bike_price = bike_cost
        self.sale_profit += self.sel_bike_price * self.markup

    def total_profit(self):
        """Calculate the cumulative profit from all sales"""
        self.store_profit += self.sale_profit
        return self.store_profit

    def sell_bike(self, bike_name):
        """Remove a sold bike from inventory"""
        self.inventory[bike_name] -= 1


class Customer:
    """Models a customer.
    
    Gives a customer name and spending money. Determines which bikes are available based on available money. Provides
    purchased bike to Shop class for inventory management."""
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bike_selection = []
        self.customer_avail = []
        self.bike_choice = None
        self.bike_sold = None

    def bikes_avail(self, bicycle):
        """Determines list of bikes within customer price range"""
        if bicycle.cost <= self.money:
            self.bike_selection.append(bicycle)

    def show_bikes_avail(self):
        """Prints list of bikes in customer's price range"""
        print("These are the bicycles available in your price range:")
        for bicycle in self.bike_selection:
            self.customer_avail.append(bicycle.model)
        return self.customer_avail

    def purchase(self):
        """Selects a bike for purchase, removes bike from shop inventory, calculates shop's profit, and calculates
        how much money customer has left"""
        self.bike_choice = input("Which would you like to purchase? ")
        if self.bike_choice == "Corvair":
            self.bike_sold = bike1
        elif self.bike_choice == "Airstream":
            self.bike_sold = bike2
        elif self.bike_choice == "Slipstream":
            self.bike_sold = bike3
        elif self.bike_choice == "Monty":
            self.bike_sold = bike4
        elif self.bike_choice == "Zuul":
            self.bike_sold = bike5
        elif self.bike_choice == "Ratman":
            self.bike_sold = bike6
        else:
            print("You gave an invalid selection")

        shop.indiv_sale_profit(self.bike_sold.cost)
        shop.sell_bike(self.bike_sold)

        print("{name} purchased a(n) {bike} for ${price}".format(name=self.name, bike=self.bike_sold.model, price=
                                                                self.bike_sold.cost))
        print("Money left in pocket: $" + str(self.money - self.bike_sold.cost))

        print("These are the bikes left in inventory: ")  # Remaining stock
        for i in shop.inventory:
            print(i.model, shop.inventory[i])

        print("Store profit from sale: ${}".format(shop.sale_profit))
        print("Total profit: ${}".format(shop.total_profit()))


if __name__ == "__main__":
    dan = Customer("dan", 200)
    jessie = Customer("jessie", 500)
    brock = Customer("brock", 1000)

    shop = Shop("Blannigan's Bikes")

    # Create each bike object
    bike1 = Bicycle("Corvair", 20, 150)
    bike2 = Bicycle("Airstream", 18, 200)
    bike3 = Bicycle("Slipstream", 25, 100)
    bike4 = Bicycle("Monty", 16, 400)
    bike5 = Bicycle("Zuul", 10, 800)
    bike6 = Bicycle("Ratman", 13, 650)

    shop.initial_inventory(bike1, 1)
    shop.initial_inventory(bike2, 1)
    shop.initial_inventory(bike3, 1)
    shop.initial_inventory(bike4, 1)
    shop.initial_inventory(bike5, 1)
    shop.initial_inventory(bike6, 1)

    print("Welcome to {}".format(shop.name))
    print("Here the bikes we carry:")
    for bicycle in shop.inventory:
        print("Name: {}".format(bicycle.model))
        print("Weight: {} lbs".format(bicycle.weight))
        print("Cost: ${}".format(bicycle.cost))
    print("\n")

    # Customer 1
    print("Dan's budget = ${}".format(dan.money))
    for bike in shop.show_inventory():
        dan.bikes_avail(bike)
    for item in dan.show_bikes_avail():
        print(item)
    dan.purchase()
    print("\n")

    # Customer 2
    print("Jessie's budget = {}".format(jessie.money))
    for bike in shop.show_inventory():
        jessie.bikes_avail(bike)
    for item in jessie.show_bikes_avail():
        print(item)
    jessie.purchase()
    print("\n")

    # Customer 3
    print("Brocks's budget = {}".format(brock.money))
    for bike in shop.show_inventory():
        brock.bikes_avail(bike)
    for item in brock.show_bikes_avail():
        print(item)
    brock.purchase()

