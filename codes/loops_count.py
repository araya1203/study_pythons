# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Loops count : 2
# 1 : "apple"
# 2 : "banana"
# Loops count : 3
# 1 : "apple"
# 2 : "banana"
# 3 : "cherry"
# Loops count : Q  # 종료



fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

while True:
    try:
        loops_count = int(input("Loops count : "))
    except ValueError:
        print("종료")
        continue
    
    if isinstance(loops_count, int):
        for i in range(1, loops_count + 1):
            if i > len(fruits):
                print("Index out of range.")
                break
            print(f"{i} : \"{fruits[i-1]}\"")
    else:
        print("Loops count : Q")
        break

