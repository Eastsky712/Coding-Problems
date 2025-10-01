CN = int(input()) #Computer Number
NN = int(input()) #Network Number
CR = {}
infected = [1]

for x in range(NN):
    key, value = map(int, input().split(" "))
    CR.setdefault(key, []).append(value)
    CR.setdefault(value, []).append(key)
#print(CR)

def virus(n):
    if not n in infected:
        infected.append(n)
    for next_computer in CR.get(n, []):
        #print("Inside " + str(CR[n][x]))
        if next_computer not in infected: #Recursion error prevention
            virus(next_computer)


virus(1)
#print(infected)
print(len(infected)-1)