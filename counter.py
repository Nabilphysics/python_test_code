import time

i = 0

for k in range(50):
    time.sleep(0.1)
    print('For Loop')

while True:
    for i in range(10):
        i = i + 1
        print(i)
    print('After While: ',i)
