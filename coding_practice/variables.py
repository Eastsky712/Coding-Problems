import this

first_name = "Dongmin"
last_name = "Seo"
full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}!"
print("\t" + message)

current_occupation = " Daycare? "

print(current_occupation.strip())

test_case = "abcdEFGH ijklMNOP"
print(test_case.upper())
print(test_case.lower())
print(test_case.swapcase())

famous_quote1 = "\"Be yourself; everyone else is already taken.\""
famous_quote2 = "\"I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best\""
print(famous_quote1)
print(famous_quote2)

famous_person = "Albert Einstain"
famous_quote3 = f"\"Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.\" - {famous_person}"
print(famous_quote3)

big_number_test = 1_200_500
print(big_number_test)
#Here I was testing is big_number_test would automatically turn into a string or if I had to str() it
print(f"My favorite number is {big_number_test}")