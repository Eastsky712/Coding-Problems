CN = int(input()) #Computer Number
NN = int(input()) #Network Number
CR = {}
infected = [1]

for x in range(NN):
    key, value = input().split(" ")
    key = int(key)
    CR.setdefault(key, [])
    CR[key].append(int(value))
#print(CR)

def virus(n):
    if not n in infected:
        infected.append(n)
    if not n in CR:
        return
    for next_computer in (CR[n]):
        #print("Inside " + str(CR[n][x]))
        if next_computer not in infected:
            virus(next_computer)


virus(1)
#print(infected)
print(len(infected)-1)