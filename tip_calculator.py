def tip_calculator():
    bill = float(input("How much is the restaurant bill?\n"))
    percent = float(input("What percent do you want to tip?\n"))
    tip = bill * (percent / 100)
    total_price = bill + tip
    return total_price

print(tip_calculator())
