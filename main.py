import portfolio

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
current_prices = {"AAPL": 160.25, "GOOGL": 350.75, "MSFT": 500.50}

# Расчет общей стоимости портфеля
total_value = portfolio.calculate_portfolio_value(stocks, prices)
total_value_current = portfolio.calculate_portfolio_value(stocks, current_prices)
print("Начальная стоимость портфеля акций:", total_value)
print("Общая стоимость портфеля акций:", total_value_current)

# Расчет доходности портфеля
portfolio_return = portfolio.calculate_portfolio_return(total_value, total_value_current)
print("Процентная доходность портфеля:", portfolio_return)

# Наиболее прибыльная акция
most_profitable_stock = portfolio.get_most_profitable_stock(stocks, current_prices)
print("Наиболее прибыльная акция:", most_profitable_stock)

