set_1 = {'Ram', 'Shyam', 'Indra'}
set_2 = {'Faisal', 'Fahim', 'Indra'}
set_3 = {'Rohan', 'Deepto'}

# set_1.update(set_2)
set_1 |= set_2
print(set_1)
print(set_1.intersection(set_2, set_3))
set_1.intersection_update(set_2)
print(set_1)
print(set_3)