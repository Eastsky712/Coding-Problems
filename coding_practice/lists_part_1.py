random_var = [1, 1.0, "1", '1']
print(random_var)

fruits = ["banana", "grapes", "apple", "watermelon"]
print(f"My favorite fuirt growing up was {fruits[3].title()}")

delete_test = ["stuff1", "stuff2", "stuff3"]
del delete_test[1]
print(delete_test)

names = ["Charles", "Amy", "Hitchcock", "Terry", "Gina", "Jake"]
names.insert(0, "Sculley")
names.insert(4, "Rosa")
names.append("Raymond")
print(names)


print("Original List Order:")
print(names)
print("Sorted List: ")
print(sorted(names))
print("Originial: ")
print(names)


locations = ["China", "Japan", "Thailand", "Singapore", "Malaysia"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)


numbers_again = [1,2,3,4,5,6,7,8,9,0]
print(numbers_again[1])
