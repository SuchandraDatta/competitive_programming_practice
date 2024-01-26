#Given a list of unique numbers and a good value, find count of pairs of numbers such that the difference between the two numbers is 
#equal to the given good value
#Example 1 5 3 4 2 value = 2
#Pairs = [1,3], [5,2], [4,2] total count of pairs = 3
#The input has 2 lines, line 1 has 2 numbers, first is for size of list and second is for the good value
#Line 2 is the list of space separated numbers

first_line = input()
good_value = int(first_line.split(" ")[1])
second_line = input()
numbers = second_line.split(" ")
numbers = [int(x) for x in numbers]

num_map = {}
numbers.sort() #nlogn
#Sorted numbers mean, when we go from left to right, we will find the smaller number of the pair first then the bigger one
#So for each smaller number, we store smaller_number+good_value as key and index of smaller number as value in the map
#If bigger number already exists as a key in map, then that is a pair, just update the value with the index of bigger number
# to get the required pair of indices
for index, each_num in enumerate(numbers):
  num_map[each_num+good_value] = [index]
  if each_num in num_map:
    nump_map[each_num].append(index)

output = 0
for key, value in num_map.items():
  if len(value)==2:
    output = output +1
print(output)

