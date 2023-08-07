string = "Yojulab !"
len(string)
pass

len(string)
# 9

# conditioin
"ju" in string
# True
"Not" in string
# False
"Not" not in string
# True

# slicing
string[3]
# 'u'
string[3:6]
# 'ula'
string[3:]
# 'ulab !'
string[:-2]
# 'Yojulab'
pass

# format
age = 36
txt = "My name is John, I am " + str(age)
print(txt)
txt_second = "My name is John, I am {}."
txt_second
'My name is John, I am {}.'
txt_second.format(age)
'My name is John, I am 36.'

quantity = 3    # index 0
itemno = 567    # index 1
price = 49.95   # index 2
myorder = "I want {0} pieces of item {1} for {2} dollars. I have just {2}."
myorder.format(quantity, itemno, price)
# 'I want 3 pieces of item 567 for 49.95 dollars. I have just 49.95.'
pass