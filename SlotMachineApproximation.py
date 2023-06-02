# factorial(c) computes c! = 1*2*3*...*c.

def factorial(c):
    answer = 1
    while c>1:
        answer = c * answer
        c -= 1
    return answer

# choice(c,r) computes the binomial coefficient c choose r.

def choice(c, r):
    answer = 1
    temp = c-r
    while c > temp:
        answer = answer * c
        c -= 1
    return answer/factorial(r)

# kExactly(k,MeterLength, P1) computes the probability that a bonus meter of size "MeterLength" is filled on the kth
# roll on a single reel with the success symbol having probability P1.

def kExactly(k, MeterLength, P1):
    return choice(k-1, MeterLength-1)*P1**MeterLength*(1-P1)**(k-MeterLength)

# kAtleast(k,MeterLength,P1) computes the probability that at the kth roll the bonus meter of length "MeterLength" is
# filled on a single reel with the success symbol having probability P1.

def kAtleast(k, MeterLength, P1):
    return 1 - (choice(k-1, MeterLength-1)*P1**MeterLength*(1-P1)**(k-MeterLength)+sum(choice(k, i)*P1**i*(1-P1)**
                                                                                (k-i) for i in range(0, MeterLength)))

# kExpectedBonusSevens(k,Meterlength,P1) computes the expected number of bonus sevens at the kth roll of a single reel
# given the bonus meter of length "MeterLength" is filled and the success symbol has probability P1.

def kExpectedBonusSevens(k, MeterLength, P1):
    i = MeterLength + 1
    summation = (i-MeterLength)*choice(k, i)*P1**i*(1-P1)**(k-i)
    temp = summation
    while i < k:
        temp = (temp*(i-MeterLength+1)*(k-i)*P1)/((i-7)*(i+1)*(1-P1))
        summation += temp
        i +=1
    return summation

# Choose your probability of success symbols here.

P1 = 1/24
P2 = 1/36
P3 = 1/72

# Choose the length of the bonus meter here as "MeterLength".

MeterLength = 7

# Count is the number of times the reels are spun. Note count increases by 1 at the start of the while loop to start
# at "MeterLength".

count = MeterLength - 1

# ExpectedEnd will be an approximation of the expected number of reel rolls to end the bonus feature.

ExpectedEnd = 0

# ExpectedBonusSevens will be an approximation of the expected number of bonus sevens at the end of a bonus feature.

ExpectedBonusSevens = 0

# This loop computes an approximate (bounding the infinite summation by 10000) expected value of when the bonus feature
# ends and the expected number of sevens. The outputs are:

# "count" the bound for the infinite summation of the expected value;
# "ExpectedEnd" the expected number of rolls required to end the bonus feature; and
# "ExpectedBonusSevens" the expected number of bonus sevens rolled after a bonus feature has ended.

while count < 10000:
    count += 1
    A = kExactly(count, MeterLength, P1)
    B = kExactly(count, MeterLength, P2)
    C = kExactly(count, MeterLength, P3)
    Aat = kAtleast(count, MeterLength, P1)
    Bat = kAtleast(count, MeterLength, P2)
    Cat = kAtleast(count, MeterLength, P3)
    ExpectedEnd += count * (A * Bat * Cat + B * Aat * Cat + C * Aat * Bat + A * B * Cat + A * C * Bat + B * C * Aat + A * B * C)
    if count > MeterLength:
        ExpectedBonusSevens += A * Cat * kExpectedBonusSevens(count, MeterLength, P2) +\
                          A * Bat * kExpectedBonusSevens(count, MeterLength, P3) +\
                          B * Cat * kExpectedBonusSevens(count, MeterLength, P1) +\
                          B * Aat * kExpectedBonusSevens(count, MeterLength, P3) +\
                          C * Bat * kExpectedBonusSevens(count, MeterLength, P1) +\
                          C * Aat * kExpectedBonusSevens(count, MeterLength, P2) +\
                          A * B * kExpectedBonusSevens(count, MeterLength, P3) +\
                          A * C * kExpectedBonusSevens(count, MeterLength, P2) +\
                          B * C * kExpectedBonusSevens(count, MeterLength, P1)
print(count, ExpectedEnd, ExpectedBonusSevens)
