#
# List comprehension
#

# define list
price_list = [1.09, 23.56, 57.84, 4.56, 6.78]

# define tax rate
TAX_RATE = .08

# create function that will handle work
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

# invoke map to transform the list
final_prices = map(get_price_with_tax, price_list)

# display list
print(list(final_prices))

# list comprehensions with conditionals
sentence = 'I love python because it is easy to read.'


# list comprehensions with complex
sentence = 'I love python because it is easy to read.'
