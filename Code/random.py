import time

microtime = round(time.time() * 1000000)

digits = microtime % 10

number = 0

for i in range(digits + 1):
    greater = microtime % (10**(i + 2))
    lesser = microtime % (10**(2))
    addition = (greater - lesser)/100
    number += addition

print(int(number))