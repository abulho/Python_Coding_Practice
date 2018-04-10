'''
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit
I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# Returns 6 (buying for $5 and selling for $11)

'''

def max_profit(stock_prices):
    '''
    function that takes stock_prices_yesterday and returns the best profit
    I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

    Parameters
    ----------
    stock_prices : list of stock stock_prices

    Returns
    -------
    Best profit that could have been for the given day

    '''
    min_price = stock_prices[0]
    final_profit = 0

    for price in stock_prices:
        min_price = min(min_price, price)
        profit = price - min_price
        final_profit = max(final_profit, profit)
    return final_profit

if __name__ == '__main__':
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    print(max_profit(stock_prices_yesterday))    
