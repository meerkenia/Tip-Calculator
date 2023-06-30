def tip_calculator():
    bill = float(input("How much is the restaurant bill?\n$"))
    percent = float(input("What percent do you want to tip?\n"))
    tip = bill * (percent / 100)
    total_price = bill + tip
    return f"The total price is: ${round(total_price,2)}"

print(tip_calculator())
