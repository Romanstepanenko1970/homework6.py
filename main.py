my_dict ={'Roma': 1970,'Pasha': 1979, 'Anna': 1980, 'Rita': 1999}
print(my_dict)
print(my_dict['Pasha'])
print(my_dict.get('Alex'))
my_dict.update({'Denis': 1979,
               'Artem': 2000})
my_dict.pop('Rita')
print(my_dict)
my_set ={1, 2, 3, 4, 1, 22, 3, 4, 8, 'apple', 'Anna', 'apple'}
print(my_set)
my_set.add(5)
my_set.add('Denis')
my_set.remove('Anna')
print(my_set)