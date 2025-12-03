"""
Getting potion time: time += (skill[i] * mana[j])

There are two bigs questions that are needed to solve this problem
- How should you find if the started time wouldn't interfer with previous potion mkaing
- When should you start your next time? -10? divide by 2? What would give a outcome where
    you don't have to constantly check

1: Maybe I have a temp array of the previous potion times which will check if the next potion
    is done too fast and if so change the starting time depending on that.
2: Maybe I calculate the amout of time it will take a potion, and somehow subtract it from the
    previous potion times which might endup with a answer.

    
2 testing
0: 5 30 40 60
52: 1 6 8 12
    52 53 58 60 64
54: 4 24 32 48
    54 58 78 86 102
86: 2 12 16 24

subtract from previous potion and which ever one is the highest, you set that as the starting time
should work 


new probelm
if time it takes for 2nd potion is longer then first potion complete then what should happen?

0: 3 8 11 20
    30 80 110 200
33: 63 113 143 233
   21 56 77 140
93: 123 158 170 233
   9 24 33 60
173: 184 197 206 233

28 63 91
36 81 117 + 27
:63 108 144
32 72 104 + 76
:108 148 180

There are too many cases where it seems to be reaching an error
My opinion is that the overall structure that I laid out in the beginning is incorrect

I think I need to think of another solution


Lets think this through logically, when does the time need to start? It need to start at the maximum time 
where it allows wizards 0-n to continuously work one after another. Now before I thought that there was a clear
pattern which would find all the answers. I didn't realy fact check which got me in this situation. 
In order for all the wizards to continiuosly work, they need to make sure that they aren't working on the 
previous potion. When you see example 1, you can see that there is always one point in the time kept where its
the same as the next potion previous wizards finish time. 


skill = [1,5,2,4]
mana = [5,1,4,2]
dp = [[0 for _ in range(len(mana))] for _ in range(len(skill))]

total = 0
for y in range(len(mana)):
    total += (skill[0] * mana[y])
    dp[0][y] = total

for x in range(1, len(skill)):
    for y in range(len(mana)):
        if y == 0:
            dp[x][y] = dp[x-1][y] + (skill[x] * mana[y])
        else:
            dp[x][y] = max(dp[x-1][y], dp[x][y-1]) + (skill[x] * mana[y])
        
print(dp)
print(dp[-1][-1])

skill = [4,5,4]
mana = [7,9,8]
main = []
time = 0
finish = [0]*len(skill)
for i in range(len(mana)):
    # This is a indictator for the start time
    #print("Start time: " + str(time))
    start_time = time

    # Appends to a list the amount of time it would take to 
    # Have all the wizards finish brewing
    for skilz in skill:
        time += (skilz * mana[i])
        main.append(time)
    print(main)

    # Finds the required time for the next batch of potions

    # Substracts the time from the previous batch and finds the max
    if i < len(mana) - 1:
        max = 0
        temp_time = 0
        for x in range(len(skill) - 1):
            temp_time += (skill[x] * mana[i + 1])
            max_time = main[x + 1] - temp_time
            if max < max_time: 
                max = max_time
        print(str(i) + ":" + str(max))
        print(time)
        if max == start_time:
            time = skill[0] * mana[i]
        else:
            time = max

        main = []
print(main[-1])


skill = [4,5,4]
mana = [7,9,8]
n = len(skill)
m = len(mana)

# Step 1: precompute cumulative wizard times per potion
cum_time = [[0]*n for _ in range(m)]
for j in range(m):
    cum_time[j][0] = skill[0]*mana[j]
    for w in range(1, n):
        cum_time[j][w] = cum_time[j][w-1] + skill[w]*mana[j]

# Step 2: compute earliest start times
start = [0]*m  # start time of each potion at wizard 0

for j in range(1, m):
    # potion j cannot start before potion j-1 clears all wizards
    max_delay = 0
    for w in range(n):
        # delay needed so potion j doesn't catch up to potion j-1 at wizard w
        delay = start[j-1] + cum_time[j-1][w] - cum_time[j][w-1] if w > 0 else start[j-1] + cum_time[j-1][0]
        if delay > max_delay:
            max_delay = delay
    start[j] = max_delay

# Step 3: compute final finish time
finish_times = [0]*n
for w in range(n):
    finish_times[w] = start[-1] + cum_time[-1][w]

total_time = finish_times[-1]
print(total_time) 
"""
skill = [4,5,4]
mana = [7,9,8]

n, m = len(skill), len(mana)
done = [0] * (n + 1)

for j in range(m):
    for i in range(n):
        done[i + 1] = max(done[i + 1], done[i]) + mana[j] * skill[i]
    for i in range(n - 1, 0, -1):
        done[i] = done[i + 1] - mana[j] * skill[i]
    
print(done[n])