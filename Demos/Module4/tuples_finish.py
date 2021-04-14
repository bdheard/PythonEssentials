#
# Tuples
# 


# Mutable
list_1 = ['History', 'Math', 'Physics','Chemistry','Art','Music']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Psychology'

print(list_1)
print(list_2)

# note both lists were changed!

# Tuples are immutable
# replace [] with ()

list_1 = ('History', 'Math', 'Physics','Chemistry','Art','Music')
list_2 = list_1

print(list_1)
print(list_2)

#list_1[0] = 'Psychology' # can't insert, append, etc...

#print(list_1)
#print(list_2)