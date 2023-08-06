# Расчет общей стоимости портфеля акций:
# Функция calculate_portfolio_value
# (stocks: dict, prices: dict) -> float
# принимает два аргумента:
# stocks - словарь, где ключами являются символы акций
# (например, "AAPL" для Apple Inc.),
# и значениями - количество акций каждого символа.
# prices - словарь, где ключами являются символы акций,
# а значениями - текущая цена каждой акции.
# Функция должна вернуть общую стоимость портфеля акций на
# основе количества акций и их текущих цен.

# Расчет доходности портфеля:
# Функция calculate_portfolio_return
# (initial_value: float, current_value: float) -> float
# принимает два аргумента:
# initial_value - начальная стоимость портфеля акций.
# current_value - текущая стоимость портфеля акций.
# Функция должна вернуть процентную доходность портфеля.

# Определение наиболее прибыльной акции:
# Функция get_most_profitable_stock
# (stocks: dict, prices: dict) -> str принимает два аргумента:
# stocks - словарь с акциями и их количеством.
# prices - словарь с акциями и их текущими ценами.
# Функция должна вернуть символ акции (ключ), которая
# имеет наибольшую прибыль по сравнению с ее начальной
# стоимостью.Начальная стоимость - первый вызов calculate_portfolio_value,
# данные из этого вызова следует сохранить в защищенную переменную на
# уровне модуля.

# Тестирование модуля:
# Напишите небольшую программу, которая импортирует модуль
# "portfolio.py" и демонстрирует использование всех трех
# функций.
# Создайте словари для акций и цен,
# запустите функции и выведите результаты.


initial_portfolio_value = None

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global initial_portfolio_value
    total_value = 0
    for name, quantity in stocks.items():
        total_value += quantity * prices[name]
    if initial_portfolio_value is None:
        initial_portfolio_value = total_value
    return total_value

def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return (current_value - initial_value) / initial_value * 100

def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    profits = {stock: stocks[stock] * prices.get(stock) for stock in stocks}
    return max(profits, key=profits.get)

if __name__ == '__main__':
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 150.25, "GOOGL": 250.75, "MSFT": 300.50}
    current_prices = {"AAPL": 160.25, "GOOGL": 350.75, "MSFT": 500.50}
    # Расчет общей стоимости портфеля
    total_value = calculate_portfolio_value(stocks, prices)
    total_value_current = calculate_portfolio_value(stocks, current_prices)
    print("Начальная стоимость портфеля акций:", total_value)
    print("Общая стоимость портфеля акций:", total_value_current)

    # Расчет доходности портфеля
    portfolio_return = calculate_portfolio_return(total_value, total_value_current)
    print("Процентная доходность портфеля:", portfolio_return)

    # Наиболее прибыльная акция
    most_profitable_stock = get_most_profitable_stock(stocks, current_prices)
    print("Наиболее прибыльная акция:", most_profitable_stock)

