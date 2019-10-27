
for i in range(1,16):
    if (i%3)==0 and (i%15)!=0:
        print('fizz')
    elif (i%5)==0 and (i%15)!=0:
        print('buzz')
    elif (i%15)==0:
        print('fizz-buzz')
    else:
        print(i)







