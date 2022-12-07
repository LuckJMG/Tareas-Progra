def revisarStock(yesterday_stock, today_sales, desired_stock):
    # Constants
    MIN_STOCK = 7

    # Calculate total sales per product
    total_sales = {}
    for sales in today_sales:
        for product in sales:
            if product not in total_sales:
                total_sales[product] = 0
            total_sales[product] += sales[product]

    # Calculate actual stock
    actual_stock = {}
    for product in total_sales:
        if product not in actual_stock:
            actual_stock[product] = 0
        actual_stock[product] = yesterday_stock[product] - total_sales[product]

    # Determinate the amount of stock to buy
    stock_buy = []
    amount_list = []
    for product in actual_stock:
        if actual_stock[product] < MIN_STOCK:
            stock_buy.append([product, desired_stock[product] - actual_stock[product]])
            amount_list.append(desired_stock[product] - actual_stock[product])

    # Organize stock list from greatest to lowest stock to buy
    count = len(amount_list)
    ordered_stock = []
    while count > 0:
        index = amount_list.index(max(amount_list))
        ordered_stock.append(stock_buy[index])
        del stock_buy[index]
        del amount_list[index]
        count -= 1

    return ordered_stock
