'''
*****
****
***
**
*
'''
i=5
while i>=1:
    j=1
    while j<=i:
        print('*', end = "")
        j=j+1
    i=i-1
    print()

'''
*
**
***
****
*****
'''
print('next pattern---------------')

i=1
while i<=5:
    j=1
    while j<=i:
        print('*', end="")
        j=j+1
    i=i+1
    print()


'''
*
*
**
***
*****
********
'''
print('fibo..')
first =0
second =1
third=second+first 
while third<=100:
    c=1
    while c<=third: #1<=1
        print('*', end="")
        c=c+1 #c=0
    print(third)
    first =second #first =1
    second =third # second =1
    third=second+first #2
    
    print()    
print('Done')
        














