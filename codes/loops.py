thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for item in items:
#     pass
for fruit in thislist:
    print(fruit)
pass
# range(2, 10)    
# for(int i=2;i < 10; i++){ // java for
#     print(i)
# }
for i in range(2,10):   # python for
    print(i)

#  while
first = 3
while (first < 6) :
    pass
    print('while count {}'.format(first))
    first = first + 1

# list with numbering    
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# enumerate 원리 이해
fruits_enumerate = enumerate(fruits)
# (3, 'orange')
next(fruits_enumerate)
# (4, 'kiwi')
next(fruits_enumerate)
# (5, 'melon')
next(fruits_enumerate)
# (6, 'mango')
# next(fruits_enumerate)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# StopIteration

# list with numbering    
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)
for index_fruit in fruits_enumerate:    # 튜플 묶음
    print(index_fruit)
    pass

fruits_enumerate = enumerate(fruits)
fruit_print_format = "number: {0}, fruit name : {1}"
for (index, fruit) in fruits_enumerate:    # 튜플 분리
    print(fruit_print_format.format(index, fruit))
    pass
pass
