# Variables
size = int(input())
product_list = []
price_list = []
shopping_list = []

# Input list
while size > 0:
    product_list.append(input())
    price_list.append(int(input()))
    size -= 1

tmp = list(price_list)

# Organize shopping list
for i in range(len(product_list)):
    index = price_list.index(min(tmp))
    shopping_list.append(product_list[index])
    del tmp[index]
    tmp.insert(index, 99999999999999)

# Output
print(str(shopping_list))
