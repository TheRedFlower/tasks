import math
total = 0
ask = int(input('press "0" to stop: '))
total += ask
while ask != 0:
    ask = int(input('press "0" to stop: '))
    total += ask
print('Number: ', round(total, 100))