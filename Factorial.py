number=int(input('Input integer number '))
factorial=1
for item in range(1,number):
    factorial*=number
    number-=1

print('Factorial =',factorial)
