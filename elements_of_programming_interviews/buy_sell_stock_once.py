from math import inf
a = [310,315,275,295,260,270,290,230,255,250]

min_price = inf
max_profit = 0

for price in a:
	max_profit = max(max_profit, price - min_price)
	min_price = min(min_price, price)

print(max_profit)