from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        self.wallet = money
        self.__order = None
        super().__init__(name, phone, email, address)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f"{self.name} placed an order {order.items}")

    def eat_food(self, order):
        pass

    def pay_for_order(self, amount):
        # TODO: submit amount to manager
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, stars):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name)
        self.phone = phone
        self.email = email
        self.address = address
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department

    def receive_salary(self, payment_amount):
        self.due -= payment_amount

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department, cooking_item)
        self.cooking_item = cooking_item

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)

    def take_order(self):
        pass
    
    def transfer_order(self):
        pass

    def serve_food(self):
        pass

    def receive_tips(self, amount):
        self.tips_earning += amount

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)