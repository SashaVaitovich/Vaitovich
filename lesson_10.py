# # task 1
#
# from datetime import datetime, timedelta
#
#
# class Task:
#     def __init__(self, description, deadline):
#         self.description = description
#         self.status = False
#         self.deadline = deadline
#
#     def mark_as_done(self):
#         self.status = True
#
#     def __str__(self):
#         status_str = "выполнена" if self.status else "не выполнена"
#         return f"Задача: {self.description}, Статус: {status_str}, Срок: {self.deadline}"
#
#
# class Project(Task):
#     def __init__(self, name):
#         super().__init__(name, None)
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def show_tasks(self):
#         print(f"Задачи проекта '{self.description}':")
#         for task in self.tasks:
#             print(task)
#
#
# class ProjectManager:
#     def __init__(self):
#         self.projects = []
#
#     def create_project(self, name):
#         project = Project(name)
#         self.projects.append(project)
#         return project
#
#
# # task 2
#
# class Passenger:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# class Ticket:
#     def __init__(self, passenger, route):
#         self.passenger = passenger
#         self.route = route
#
#     def __str__(self):
#         return f"Ticket for {self.passenger} on route {self.route}"
#
#
# class Flight:
#     def __init__(self):
#         self.reserved_tickets = []
#
#     def reserve_ticket(self, passenger, route):
#         ticket = Ticket(passenger, route)
#         self.reserved_tickets.append(ticket)
#         return ticket
#
#     def cancel_reservation(self, ticket):
#         if ticket in self.reserved_tickets:
#             self.reserved_tickets.remove(ticket)
#             return True
#         else:
#             return False
#
#     def display_reserved_tickets(self):
#         if not self.reserved_tickets:
#             print("No tickets reserved.")
#         else:
#             print("Reserved Tickets:")
#             for ticket in self.reserved_tickets:
#                 print(ticket)
#
#
# class Airline:
#     def __init__(self):
#         self.flights = []
#
#     def create_flight(self):
#         flight = Flight()
#         self.flights.append(flight)
#         return flight
#
#     def display_flights(self):
#         if not self.flights:
#             print("No flights available.")
#         else:
#             print("Available Flights:")
#             for i, flight in enumerate(self.flights, start=1):
#                 print(f"Flight {i}")
#                 flight.display_reserved_tickets()


# task 3

# from abc import ABC, abstractmethod
#
#
# class Alive(ABC):
#     def __init__(self, max_age: int, food_required: int):
#         self.age = 0
#         self.max_age = max_age
#         self.food_required = food_required
#
#     @property
#     @abstractmethod
#     def is_alive(self, food_available: int) -> bool:
#         pass
#
#     @abstractmethod
#     def eat(self, food_available: int):
#         pass
#
#
# class Plant(Alive):
#     def __init__(self, max_age: int = 100, food_produced: int = 10):
#         super().__init__(max_age, food_required=0)
#         self.food_produced = food_produced
#
#     def is_alive(self, food_available: int) -> bool:
#         return self.age < self.max_age
#
#     def eat(self, food_available: int):
#         self.age += 1
#
#
# class Rabbit(Alive):
#     def __init__(self, max_age: int = 10, food_required: int = 2):
#         super().__init__(max_age, food_required)
#
#     def is_alive(self, food_available: int) -> bool:
#         return self.age < self.max_age and food_available >= self.food_required
#
#     def eat(self, food_available: int):
#         if food_available >= self.food_required:
#             food_available -= self.food_required
#             self.age += 1
#
#
# class Fox(Alive):
#     def __init__(self, max_age: int = 8, food_required: int = 3):
#         super().__init__(max_age, food_required)
#
#     def is_alive(self, food_available: int) -> bool:
#         return self.age < self.max_age and food_available >= self.food_required
#
#     def eat(self, food_available: int):
#         if food_available >= self.food_required:
#             food_available -= self.food_required
#             self.age += 1
