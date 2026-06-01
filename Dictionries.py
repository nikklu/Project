d={'name':'nikhil',
   'marks':90,'grade':'c'}
print(d.keys())#dict_keys(['name', 'marks'])
print(d.values())#dict_values(['nikhil', 90])
print(d.items())#dict_items([('name', 'nikhil'), ('marks', 90)])
print(d.get('marks'))#it will returns the marks
print(d.update({'marks':82}))
print(d.pop('grade'))
print(d.popitem())#it delete last inserted item
#print(d.clear())

print(d)