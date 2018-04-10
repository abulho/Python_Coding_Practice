def possible_combinations_change(amount_left, coins, index=0):
    '''This function will return the number of ways you can make exact change, given a amount
    and some denominations of coins

    Paramters:
    ---------
    amount_left = To begin, this will be the amount to start with, at each recursive step, this will
                  updated base on the coin denomination in consideration
    coin = This is denomination of coins to consider
    index = This is the index to start the calculations. Initiates at 0 and will go through all the coins

    Returns:
    -------
    The number of ways you can make change, given a total amount, and coin denominations

    '''
    # this is the base case
    # example we are trying to make change for 4, and we hit 4
    if amount_left == 0:
        return 1

    # this is the case when we use a larger coin
    # example we trying to make change for 4 and we hit a 5
    if amount_left < 0:
        return 0

    # this is the case when we run out of coins
    if index == len(coins):
        return 0

    # printing out the amount left and what is being used to make change
    print('making change for {} with {}'.format(amount_left, coins[index:]))

    # getting the current coin
    current_coin = coins[index]

    number_of_ways = 0
    while amount_left >= 0:
        number_of_ways = number_of_ways + possible_combinations_change(amount_left, coins, index + 1)
        amount_left = amount_left - current_coin

    return number_of_ways

# testing the function
if __name__ == '__main__':
    coins = [1,2,3]
    amount = 4
    ways = possible_combinations_change(amount,coins)
    print('Number of ways to make change for {} with {} is {}'.format(amount, coins, ways))
