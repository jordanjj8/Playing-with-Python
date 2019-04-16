# Jordan Leung
# 2/12/2019

#numbers = [number for number in range(1,21)]
#print(numbers)

#for number in range(1,21):
#    print(number)


numbers = list(range(1,1000001))
#print(numbers)
max_num = max(numbers)
min_num = min(numbers)
sum_num = sum(numbers)
print(str(max_num) + " " + str(min_num) + " " + str(sum_num))
print(max_num)

cubes = [num**3 for num in range(1,11)]
print(cubes)