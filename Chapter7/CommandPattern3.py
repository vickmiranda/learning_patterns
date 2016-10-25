from abc import ABCMeta, abstractmethod


class Order(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


# Concrete classes are below: buy and sell stocks
class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# The receiver object is represented by the stocktrade
class StockTrade(object):
    def buy(self):
        print 'buying stocks'

    def sell(self):
        print 'selling stocks'


# The invoker is the agent/middleman trading the stocks
class Agent(object):
    def __init__(self):
        self.__orderQueue = []

    def place_order(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == '__main__':

    stock = StockTrade()
    buy = BuyStock(stock)
    sell = SellStock(stock)

    agent = Agent()
    agent.place_order(buy)
    agent.place_order(sell)


