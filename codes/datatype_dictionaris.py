# 초기화 방법
thisdict = {}    # empty inital
thisdict = dict() # empty inital
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

len(thisdict)
# 3/
type(thisdict)
# <class 'dict'>
thisdict['model']
# 'Mustang'
thisdict.model
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'model'
thisdict['brand'] = "Yojulab"
thisdict.keys()
# dict_keys(['brand', 'model', 'year'])
type(thisdict.keys())
# <class 'dict_keys'>
thisdict.values()
# dict_values(['Yojulab', 'Mustang', 1964])

dict_format = "key : {1}, value : {0}"
for key, value in thisdict.items():
    print(dict_format.format(value, key))
    pass
pass

# add item in dict
thisdict['color'] = 'Red'
# remove item in dict
del thisdict['year']
del thisdict
