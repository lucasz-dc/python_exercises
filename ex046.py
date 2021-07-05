from time import sleep

for c in range(10, -1, -1):
    sleep(1)
    print(c, end=' ')

sleep(1)

print('\033[1;31mBOOOM!\033[m')
