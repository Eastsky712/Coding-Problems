magic_types = ["Water","Fire","Ground","Wind","Metal","Light","Dark"]
for magic_type in magic_types:
    print(f"I can use the Magic Type {magic_type.upper()}")
    print(f"{magic_type} is the best Magic Type! \n")

print("Shut up")

names = ["Bob", "Karl", "Grace"]

for name in names:
    print(f"My name is {name}")
print(f"{name} is my first name")

digits = [0,1,2,3,4,5,6,7,8,9]
print(max(digits))
print(min(digits))
print(sum(digits))

squares = [value ** 2 for value in range(1,11)]
print(squares)

million = [value for value in range(1,1000000)]
print(max(million))
print(min(million))
print(sum(million))

odds = [value for value in range(1,21,2)]
print(odds)

multiples_of_three = [value for value in range(3,30,3)]
print(multiples_of_three)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)

list_slicing = [value for value in range(1,101)]
print(list_slicing[30:50])
print(list_slicing[-20:])
print(list_slicing[1:40:3])

for num in list_slicing[:8]:
    print(num)

my_foods = ["meat","bread","jelly"]
friends_foods = my_foods #This isn't a copy but instead a gives a different variable to associate with the same list
brothers_foods = my_foods[:] #This coies the contents of the list to a new list

print(friends_foods)
print(brothers_foods)
print(my_foods)
my_foods.append("noodles")
friends_foods.append("soup")
brothers_foods.append("cheese")
print(friends_foods)
print(brothers_foods)
print(my_foods)



#Tuples

dimensions = (160, 320)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)
#dimensions[0] = 200 doesn't work because it is a tuple

dimensions = (200, 400)
print("Modified Dimensions:")
for dimension in dimensions:
    print(dimension)

restaurant_foods = ("Meat","Noodle","Bread","Sushi","Rice")
for food in restaurant_foods:
    print(food)
#restaurant_foods[0] = "Tofu" Works (as in doesn't work but that was the point)
restaurant_foods = ("Tofu","Dessert","Bread","Sushi","Rice")
    #Is a tab just four spaces?
    #Yes it is!
    #Apparently A text editor usually converts a tab into 4 spaces
    #if I want a actual tab, it would be \t

