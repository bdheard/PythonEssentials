#
# List comprehension
#

# define list
price_list = [1.09, 23.56, 57.84, 4.56, 6.78]

# define tax rate
TAX_RATE = .08

# create function that will handle work
def get_price_with_tax(price_list):
    return price_list * (1 + TAX_RATE)

# use list comprehensions to transform list of prices
final_prices = [get_price_with_tax(price) for price in price_list]

# display list
print(final_prices)

# list comprehensions with conditionals
sentence = 'I love python because it is easy to read.'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)

# list comprehensions with complex
sentence = 'I love python because it is easy to read.'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]

print(consonants)