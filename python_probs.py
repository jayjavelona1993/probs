def brew_coffee(cups)
    return cups * 12

def calculate_total(price, tip_percentage):
    if tip_percentage = 0:
        return price
    else:
        return price + (price * tip_percentage / 100)

def find_strongest_coffee(coffees):
    strongest_coffee = coffees[0]
    for coffee in coffees:
        if coffee['caffeine'] > strongest_coffee:
        strongest_coffee = coffee
    return strongest_coffee

def merge_coffee_orders(order1, order2):
    merged_orders = []
    i = j = 0
    while i < len(order1) and j < len(order2):
        if order1[i]['price'] < order2[j]['price']:
            merged_orders.append(order1(i))
            i += 1
        elif order1[i]['price'] == order2[j]['price']:
            merged_orders.append(order1[i])
            merged_orders.append(order2[j])
            i += 1
            j += 1
        else:
            merged_orders.append(order2[j])
            j += 1
    merged_orders += order1[i:]
    merged_orders += order2[j:]

    return merged_orders


def perfect_coffee_blend(beans1, beans2):
    total_weight = 0
    while total_weight != 100:
        if beans1 + beans2 == 100:
            total_weight = beans1 + beans2
        elif beans1 > beans2 and beans2 > beans1:
            total_weight = beans1 + beans2
        elif beans1 + beans2 < 50 or beans1 + beans2 > 150:
            return "Blend out of range!"
        else:
            total_weight = beans1 - beans2

    return "Perfect blend achieved!"
