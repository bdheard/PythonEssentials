#
# Collections
# 

# Create 3 dictionary objects
john = {}
john['first'] = 'John'
john['last'] = 'Doe'

james = {}
james['first'] = 'James'
james['last'] = 'Smith'

charles = {}
charles['first'] = 'Charles'
charles['last'] = 'Johnson'

david = {}
david['first'] = 'David'
david['last'] = 'Somebody'

# Add dictionary objects to list object
people = []
people.append(john)
people.append(james)
people.append(charles)
people.append(david)
people.append({'first': 'Bill', 'last': 'Gates'})

# Slicing
print(people)
print(people[2])
print(people[1:3])
print(people[:3])

# Operations

#Length
print(len(people)) # Get the number of items

# insert
people.insert(0, {'first': 'Luke', 'last': 'Skywalker'}) # Insert before index
print(people)

# extend
people_2 = [{'first': 'Han', 'last': 'Solo'},{'first': 'Lea', 'last': 'Skywalker'}]
people.extend(people_2)
print(people)

# remove
courses = ['History', 'Math', 'Physics','Chemistry','Arts','Music']
courses.remove('Math')
print(courses)

# use list as task of queue
# pop will remove the last value of the list.
# pop will return the value it removes
popped = courses.pop()
print(popped)
print(courses)

# reverse
courses.reverse()
print(courses)

# sort in place
courses.sort()
print(courses)

nums = [10, 1, 5, 2, 8, 7]
nums.sort()
print(nums)

# sort descending order
courses.sort(reverse = True)
nums.sort(reverse = True)
print(courses)
print(nums)

# sort without chaning original list
courses_sorted = sorted(courses)
print(courses_sorted)

# math operations

print(min(nums))
print(max(nums))
print(sum(nums))

# filtering
print(courses.index('Arts'))
print('Art' in courses)
print(courses[-1]) #-1 last one
#print(courses[20]) # error index out of range

#convert to string
courses_str = ', '.join(courses)
print(courses_str)

# convert string to list
new_courses_list = courses_str.split(', ')
print(new_courses_list)

