fruits = ["apple", "banana", "cherry","mango"]
for fruit in fruits:
    print(fruit)

print(fruits[0])
print(fruits[1])

fruits[1]="watermelon"
fruits.insert(3,"pineapple")

fruits.remove("cherry")
print(fruits)
fruits.pop(2)
print(fruits)

i= 0
while i < len(fruits):
    print(fruits[i])
    i += 1

    fruits.sort()
print(fruits)

fruits.reverse()
fruits.append("grape")
print(fruits)
new_fruits = fruits.copy()
print(new_fruits)
number=[1,2,3,4,5,6,7,8,9,10]
summation = 0
for i in number:
    summation += i
print(summation)
