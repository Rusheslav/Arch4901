from datetime import datetime


class BusStop:
    bus_stops = []  # список для хранения остановок

    id_: int
    name: str
    zone: int
    has_ticket_office: bool

    def __init__(self, name, zone, has_ticket_office=False):
        self.id_ = len(
            BusStop.bus_stops) + 1  # Допустим, что удалять остановки из списка нельзя, поэтому задвоение id исключено
        self.name = name
        if 1 <= zone <= 10:
            self.zone = zone
        else:
            raise ValueError('Значение поля "Зона" должно быть от 1 до 10')
        self.has_ticket_office = has_ticket_office
        BusStop.bus_stops.append(self)


class Ticket:
    tickets = []  # список для хранения билетов

    id_: int
    departure_bus_stop: BusStop
    arrival_bus_stop: BusStop
    departure_time: datetime
    user_id: int
    is_used: bool
    price: float
    seat: int

    def __init__(self, departure_bus_stop, arrival_bus_stop, departure_time, user_id, seat, is_used=False):
        self.id_ = len(
            Ticket.tickets) + 1  # Допустим, что удалять билеты из списка нельзя, поэтому задвоение id исключено
        self.departure_bus_stop = departure_bus_stop
        self.arrival_bus_stop = arrival_bus_stop
        self.departure_time = departure_time
        self.user_id = user_id
        self.price = 20.0 * (1 + abs(
            self.departure_bus_stop.zone - self.arrival_bus_stop.zone))  # Перемещение внутри одной зоны стоит 20 р., заезд в каждую новую зону + 20 р.
        self.seat = seat
        self.is_used = is_used
        Ticket.tickets.append(self)

    def __str__(self):
        return (f'Билет за номером {self.id_}\n'
                f'Маршрут: "{self.departure_bus_stop.name}" - "{self.arrival_bus_stop.name}"\n'
                f'Пассажир: {User.users[self.user_id-1]}\n'
                f'Время отправления: {self.departure_time}')

    def mark_as_used(self):
        if not self.is_used:
            self.is_used = True
            print("Билет помечен как использованный")
        else:
            print("Билет уже помечен как использованный.")


class User:
    users = []  # список для хранения пользователей

    def __init__(self, name, login, password_hash, account_id):
        self.id_ = self.id_ = len(
            User.users) + 1  # Допустим, что удалять билеты из списка нельзя, поэтому задвоение id исключено
        self.name = name
        self.tickets = []
        self.login = login
        self.password_hash = password_hash
        self.account_id = account_id
        User.users.append(self)

    def __str__(self):
        return f'{self.name}'

    def buy_ticket(self, ticket):
        if ticket.price <= Account.get_account_balance(self.account_id):
            self.tickets.append(ticket)
            Account.update_balance(self.account_id, -ticket.price)
        else:
            print("На счету пользователя недостаточно средств для покупки билета.")


class Account:
    accounts = []  # список для хранения счетов

    def __init__(self, balance):
        self.user_account_id = len(Account.accounts) + 1
        self.balance = balance
        Account.accounts.append(self)

    @staticmethod
    def get_account_balance(account_id):
        if account_id > len(Account.accounts) or account_id < 1:
            raise ValueError(f'Счёт с id {account_id} не найден')
        return Account.accounts[account_id - 1].balance

    @staticmethod
    def update_balance(account_id, amount):
        if account_id > len(Account.accounts) or account_id < 1:
            raise ValueError(f'Счёт с id {account_id} не найден')
        Account.accounts[account_id - 1].balance += amount
