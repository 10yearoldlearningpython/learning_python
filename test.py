before = "Sale $34.99"
after = before.replace("Sale $", '')
number = float(after)

print(number*3)
