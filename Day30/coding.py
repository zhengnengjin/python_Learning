def cheap_p(price_list, upper_price):
	for price in price_list:
		if price > upper_price:
			print("请输入小于%d元的商品"%upper_price)
			return False
	return True
	
def calculate_price(prices_list, budget):
	sum_price = 0
	for price in prices_list:
		sum_price += price
		if sum_price > budget:
			sum_price -= price
			print("总价格为：",sum_price)
			break
budget = int(input("请输入预算金额："))
prices = input("请输入每种商品的价格，用空格分隔：")

prices_list = prices.strip().split(' ')
for i in range(len(prices_list)):
    prices_list[i] = int(prices_list[i])

print(prices_list)
prices_list.sort()

if cheap_p(prices_list, 10000):
    calculate_price(prices_list, budget)