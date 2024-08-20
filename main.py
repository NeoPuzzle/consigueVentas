import time
#My first print !!
print("I like pizza")

full_name = "Renzo B."
age = 35
gpa = 3.2
is_junior = True

print(f"Hello I'm {full_name}")
print(f"I have {age} years old")
print(f"My gpa is {gpa}")


if is_junior:
    print(f"{full_name} is junior")
else:
    print(f"{full_name} isn't junior")

friends = 9

friends += 2
print(friends)
friends -= 2
print(friends) 
friends  /=2
print(friends)
friends //= 2
print(friends)

remainding = 10
remainding %= 3
print(remainding)


#TypeCasting
print(type(full_name))
age = float(age)
print(age)


# nameInput = input("Enter your name: ")
# print(f"Hello {nameInput}!!")

numberIf = 10

if numberIf >= 9:
    print("2 decimales")
elif numberIf >= 20:
    print("mayor de 20")
elif numberIf < 0:
    print("negative number")
elif numberIf == 0:
    print("Zero")
else:
    print("buh")


temp = -2
is_raining = False
is_sunny = False

if temp > 35 or temp < 0 or is_raining:
    print("Event canceled")
else: 
    print("event schedulle")

if temp >= 28 and is_sunny:
    print("It is Hot!!!")
elif temp <= 0 and not is_sunny:
    print("Is cool")
else:
    print("It is sunny")


# name = input("Enter your name: ")

# while name == "":
#     name = input("Enter your name: ")


for i in range(10, 21, 2):
    print(i)
    # time.sleep(1)

for i in range(10, 1, -2):
    print(i)

for letter in full_name:
    print(letter)

#List[]  = mutable, most flexible
fruits =["apple", "banana", "coconuts"]
fruits[0] = "mango"
# fruits.append("pineapple")
# fruits.remove("banana")
# fruits.pop(0)
# fruits.clear()


for fruit in fruits:
    print(fruit, end=" ")

#Tuple () = inmutable, faster
fruitsTuple =("apple", "banana", "coconuts")
for fruitple in fruitsTuple:
    print(fruitple)

#Set {}  = mutable (add/remove), unordered
#           No duplicates, best for menbership testing

fruitsSet ={"apple", "banana", "coconuts"}
fruitsSet.add("mango")
# fruitsSet.remove("coconuts")
# fruitsSet.pop()
# fruitsSet.clear()

if "banana" in fruitsSet:
    print("banana was found")
else:
    print("banana is not found")

for fruitset in fruitsSet:
    print(fruitset, end=" ")