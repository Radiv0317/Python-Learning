primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

for x in range (5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)

count = 0
while count < 5:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range (10):
    if x % 2 == 0:
        continue
    print(x)

count=0
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of break but not due fail in condition")