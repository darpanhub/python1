print([num for num in range(1, 101)])

print ('even nos below 100')
for num in range(1, 101):
    if num %2==0:
        print(num, end='')

even_numbers= [num for num in  range(1,101) if num %2 ==0]       
print(even_numbers) 

# print table
# print('Enter your number')
# n= int(input())
# for i in range (1, 11):
#     print('{} * {} = {}'.format(n, i, n*i))

name = 'darpan'

print(name[3])

newname = []
for letter in name:
    newname.append(letter)
print(newname)    
