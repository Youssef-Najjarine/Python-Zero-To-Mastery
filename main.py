
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num for num in range(0,100) if num % 2 == 0]
my_set = {char for char in 'hello'}

print('my_list: ', my_list)
print('my_list2: ', my_list2)
print('my_list3: ', my_list3)
print('my_list4: ', my_list4)
print('my_set: ', my_set)


simple_dict = {
  'a': 1,
  'b': 2
}

my_dict = {k:v**2 for k,v in simple_dict.items() if v%2 ==0}

print('simple_dict.items(): ', simple_dict.values())
print('my_dict: ', my_dict)


from functools import reduce
# my_list = [1,2,3]
# your_list = (10,20,30)
# their_list = (5,4,3)
# def multiply_by2(item):
#   return item*2


# print(list(map(multiply_by2, my_list)))

# def only_odd(item):
#   return item % 2 != 0

# def accumulator(acc,item):
#   print(acc, item)
#   return acc + item

# print(list(filter(only_odd, my_list)))


# print(list(zip(my_list,your_list,their_list)))

# print(reduce(accumulator,my_list,10))


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize_names(name):
  return name.upper()
print(f'Capitalized list: {list(map(capitalize_names,my_pets))}')

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(f'Zipped List: {list(zip(my_strings,sorted(my_numbers)))}')
#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(f'Filtered List:{sorted(list(filter(lambda el: el > 50,scores)))}')
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(f'Reduced Values: {reduce(lambda acc,val: acc + val,my_numbers+scores)}')

squared_list = print(f'Squared List: {list(map(lambda num: num**2, [5,4,3]))}')

a = [(0,2), (4,3), (9,9), (10,-1)]

print(f'Sorted by Second index: {sorted(list(map(lambda tpl: tuple(sorted(tpl)),a)))}')

print(f'Sorted by Second index 2nd version: {a.sort(key=lambda x: x[1])}')

class SuperList(list):
  def __len__(self):
    return 1000


super_list1 = SuperList()
super_list1.append('apples')
print('super_list1: ', super_list1)
print(super_list1[0])
print(len(super_list1))
