

#Let's assume I have need a number 
#From 1 - 10
# I can use range to fix this. 

for number in range(1,10):
    print(number)
#something to note is that, because 10 is specified doesn't mean it prints it to the last number
#so we change it to 11
for number in range(1,11):
    print(number)
#if I want to put this number's in a list then .# 
def list_range():
    numbers = list(range(1,11))
    print(numbers)
list_range()
#adding a third argument to range, to skip numbers
for even_number in range(0,6,2):
    print(even_number)
list_item= []
for even_number in range(1,10):
    list_item.append(even_number)
list_item_= []
for item in list_item:
    list_item_.append(item + item + 1)

print(list_item_)
min = min(list_item_)
print(min)
max = max(list_item_)
print(max)

#list comprehensions
square = [value ** 2 for value in range(1,11)]

print(square[-1])
for number in square[2:8:2]:
    print(number)

#tuple items cannot be redefined except the variable itself is redifined. 
tuple_list = 3,4,3,5

#example
tuple_list = 4,3,4,6
print(tuple_list)



