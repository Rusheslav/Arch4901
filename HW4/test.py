from datetime import datetime

from classes import BusStop, Ticket, User, Account

if __name__ == "__main__":
    # Создадим две остановки
    stop_one = BusStop("Детская поликлиника", 1)
    stop_two = BusStop("Вокзал", 10, True)

    # Создадим аккаунт и положем на него 1000.0 рублей
    account1 = Account(1000.0)

    # Создадим пользователя
    mikhail = User("Михаил Горшенев", "Gorshok", hash("Knyaz_loh"), account1.user_account_id)

    # Создадим билет
    ticket1 = Ticket(stop_one, stop_two, datetime.now(), mikhail.id_, -1)

    # Купим билет
    mikhail.buy_ticket(ticket1)

    # Проверим, что билет куплен пользователем
    print(*mikhail.tickets)

    # Проверим, что со счета пассажира списалась нужная сумма
    print("\n\nБыло: 1000 р.")
    print(f"Списалось: {ticket1.price}")
    print(f"Осталось: {account1.balance}")
