from datetime import date, timedelta


def calculate_price(segment, end, start, price):
    if segment == 1:
        return (end - start).days * price
    elif segment == 2:
        return (end - start).days * price * 1.2
    elif segment == 3:
        return (end - start).days * price * 1.4
    elif segment == 4:
        return (end - start).days * price * 1.6
    else:
        return (end - start).days * price * 2


if __name__ == '__main__':
    segment = 1
    end = date.today()
    start = end - timedelta(days=5)
    price = 99
    print(calculate_price(segment, end, start, price))