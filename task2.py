# name = 'darpan'

# print(name[3])

# newname = []
# for letter in name:
#     newname.append(letter)
# print(newname)

# third_list = [letter for letter in name]
# print(third_list)

# for num in range (1, 101)
# print(num ,end='')


# first_list = [1,2,3,4,5,6,7,8,9]

# second_list = [num for num in first_list]
# print(second_list)


# fourth_list = [numb for numb in range(1,51)]
# print(fourth_list)

# even_numbers = [num if num % 2 == 0 else ' {} odd num' .format(num) for num in range(1, 101)]
# print(even_numbers)

# square root of list
# import math
# number_list = [2,4,8,16]
# for num in number_list:
#     print(int(math.sqrt(num)))

# #two line method
# square_root_list = [int(math.sqrt(num)) for num in number_list ]
# print(square_root_list)

#nested for loop
nestlist = []
for n in [1,2,3]:
    for y in [100, 200, 300]:
        nestlist.append(n * y)
print(nestlist) 
#another two line
first_list = [1,2,3]
second_list = [100,200,300]

result = [n * y for n in first_list for y in second_list ]
print(result)