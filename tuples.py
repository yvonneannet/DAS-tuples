
# creating a tuple
my_tuples = (10,20,30,40,50)

#creating a tuple that has only one item
number= (5,)


#adding items to a tuple.
my_list =list(number)
a= (60,70,80)
my_list = number + a
numbers= tuple(my_list)

#removing items from a tuple 
new_list = list(my_tuples)
my_list= new_list.pop()
my_tuples= tuple(new_list)

#iterating through a list
my_list= list(my_tuples)

for i in my_list:print(i+10)

my_tuples= tuple(my_list)



print(number)
print(my_tuples)



# accessing my_tuples tuple,
print(my_tuples[1])

#accessing the number tuple
print(number[0])
