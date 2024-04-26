class PlayerCharacter:
  # Class Object Attribute
  membership = True
  def __init__(self,name='anonymous',age=0):
    if (age > 18):
      self.name = name
      self.age = age

  def shout(self):
    print(f'MY NAME IS {self.name}')
    return 'done'

player1 = PlayerCharacter('Cindy',19)
player2 = PlayerCharacter('Tom',10)

print(player1.name, player1.age, player1.shout())
print(player2.name, player2.age)

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)

def oldest_cat(*args):
  return max(args)

print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')


# cats = [Cat('Tom',10),Cat('Jerry',20),Cat('Mike',30)]


# def find_oldest_cat():
#   cur_age = 0
#   oldest_cat = ''
#   for idx in enumerate(cats):
#     for (idx2,cat_to_compare) in enumerate(cats):
#       if ((idx != idx2) and (cur_age < cat_to_compare.age)):
#         cur_age = cat_to_compare.age
#         oldest_cat = f'The oldest cat is {cat_to_compare.name} and it is {cat_to_compare.age} years old'

#   return oldest_cat

# print(find_oldest_cat())
