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
