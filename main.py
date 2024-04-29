
class SuperList(list):
  def __len__(self):
    return 1000


super_list1 = SuperList()
super_list1.append('apples')
print('super_list1: ', super_list1)
print(super_list1[0])
print(len(super_list1))

