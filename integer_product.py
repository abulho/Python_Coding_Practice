'''
You have a list of integers, and for each index you want to find the product
of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a
list of integers and returns a list of the products.
'''

def interger_product(int_list):
    ''' takes in list of intergers and returns the product of
    the numbers, excluding the number at that index.

    Parameters
    ----------
    int_list: list of intergers

    Returns
    -------
    the prouct of the intergers except for the number a the given index

    Example
    -------
    [1, 7, 3, 4] should return   [84, 12, 28, 21]

    '''

    mul_list = []
    for i in enumerate(int_list):
        num_to_exclude = int_list[i[0]]
        product = 1
        for number in int_list:
            if number != num_to_exclude:
                product = product * number
        mul_list.append(product)
    return mul_list

if __name__ == '__main__':
    int_list = [1, 7, 3, 4]
    print(interger_product(int_list))
