import random

# "tests" is the number of tests performed.

tests = 100000

# "i" is the counter for test i.

i = 0

# "ExpectedRolls" will count number of rolls performed over all tests.

ExpectedRolls = 0

# "ExtraSevens" counts the number of extra sevens (above 7) over all reels and tests.

ExtraSevens = 0

# The outside loop covers all tests. For each test, the inside loop simulates a slot machine using the random.randint
# function to generate random numbers, counters C1, C2, C3 to count the number of sevens in each reel and counter
# "count" to count the number of rolls in a single simulation. ExpectedRolls is the sum of the final "counter"
# of each simulation and ExtraSevens is the sum of C1, C2, C3 over each simulation.

while i < tests:
    i += 1
    C1 = 0
    C2 = 0
    C3 = 0
    count = 0
    while C1<7 or C2<7 or C3<7:
        count += 1
        if random.randint(1,24) == 1:
            C1 += 1
        if random.randint(1,36) == 1:
            C2 += 1
        if random.randint(1,72) == 1:
            C3 += 1
    ExpectedRolls += count
    ExtraSevens += (C1 + C2 + C3 - 21)

# The expected number of rolls will be the "ExpectedRolls" divided by "tests" and the expected number of
# extra sevens will be "ExtraSevens" divided by "tests".

print(ExpectedRolls/tests,ExtraSevens/tests)


