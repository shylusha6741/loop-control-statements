# 1. First even digit from the left in 753914286
n=753914286
div=100000000
while n!=0:
    fd=n//div
    n=n%div
    if fd%2==0:
        print("First even digit: ",fd)
        break
    div=div//10

# 2.First prime number between 50 and 100
for j in range(50,101,1):
    count=0
    n=j
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
    if count==2:
        print("First Prime number between 50 and 100:",n)
        break

# 4. First number with exactly 3 divisors between 1 and 100
for j in range(1,101,1):
    count=0
    n=j
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
    if count==3:
        print("First Number with exactly 3 divisors between 1 and 100: ",n)
        break

# 7. First perfect number between 1 and 1000
for j in range(1,1001,1):
    sum=0
    n=j
    for i in range(1,n,1):
        if (n%i==0):
            sum=sum+i
    if sum==n:
        print("First perfect number between 1 and 1000 :",n)
        break

# 8. Print first 5 even numbers
count=0
for i in range(1,100,1):
    if(i%2==0):
        print(i)
        count=count+1
    if count==5:
        break

# 9. Print first 5 prime numbers
count=0
for j in range(1,100):
    n=j
    factors=0
    for i in range(1,n+1,1):
        if n%i==0:
            factors=factors+1
    if factors==2:
        print(n)
        count=count+1
    if count==5:
        break


# 10. First 3 numbers divisible by 7
count=0
for i in range(1,101,1):
    if i%7==0:
        print(i)
        count=count+1
    if count==3:
        break


# continue
# 1. Print 1–30, skipping even numbers
for i in range(1,31,1):
    if(i%2==0):
        continue
    print(i)

# 2. Print 1–40, skipping multiples of 4
for i in range(1,41,1):
    if i%4==0:
        continue
    print(i)

# Print 1–30, skipping numbers from 10–20
for i in range(1,31,1):
    if(i>=10 and i<=20):
        continue
    print(i)

# 4. Print 1–50, skipping multiples of 3
for i in range(1,51,1):
    if(i%3==0):
        continue
    print(i)

# 5. Extract 502304, skipping digit 0
n=502304
while n!=0:
    ld=n%10
    n=n//10
    if ld==0:
        continue
    print(ld,end="")

# 6. Extract 5832461, printing only even digits
n=5832461
while n!=0:
    ld=n%10
    n=n//10
    if ld%2!=0:
        continue
    print(ld)
# 7. Extract 1432578, skipping odd digits
n=1432578
while n!=0:
    ld=n%10
    n=n//10
    if ld%2!=0:
        continue
    print(ld)

# 8. Print 1–200, skipping multiples of 3 or 5
for i in range(1,201,1):
    if(i%3==0 and i%5==0):
        continue
    print(i)
# 9. Print 1–500, skipping numbers with odd digit sum
for j in range(1,501,1):
    n=j
    sum=0
    while j!=0:
        ld=j%10
        sum=sum+ld
        j=j//10
    if sum%2!=0:
        continue
    print(n)

