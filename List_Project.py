# Basic List Questions 

#1. Create a list of 5 arbitrary numerical values and print the list to the console. 
List = [ 1,2,3,4,5]
print(List)
# 2. Given a list, write code to display only the first and the last element. 
List = [1,2,3,4,5]
print('First Element of the list -',List [0] ,'Last Element Of the List - ' ,List[-1], end = ' ')

print()

# 3. Determine and print the total number of elements in a list without utilizing the built-in len() function. 
List = [ 1,2,3,4,5]
i = 0
for num in List:
    i += 1
print(f'Number of Element in the list {i}')

# 4. Modify a given list by adding a new element to its end, 
# solely using list indexing and assignment (without using the append() method). 
List = [ 1,2,3,4,5]
List += [None]
List[len(List) -1] = 6
print(List)

#5. In a pre-defined list, change the value of the element located at the
#  third index position with a new specified value. 

List = [ 1,2,3,4,5]
List[2] = 10
print(List)

# 6. Develop a script that accepts 5 distinct inputs from the user and stores
# all of them sequentially in a single list. 

List = []
for a in range (5):
    elements = input(f'Enter Input {a+1} - ')
    List.append(elements)
print("The list of inputs is:", List)

# 7. Iterate through a given list using a for loop and print each element on a new line.
List = [10,2,3,4,5]
for num in List:
    print(num)

print()

# 8. From a given list of integers, write code to print only the numbers that are even. 
List = [1,2,3,4,5,6,7,8,9,10]
for num in List:
    if num%2 == 0:
        print(num)

print()
# 9. For a given list and a target number, calculate and print the total number 
# #of occurrences of the target number within the list. 
List =[1,2,2,2,3,4,5,2,6,6]
print('occurrences of no 2 = ', List.count(2))

# 10. Calculate and print the sum of all numerical elements in
#  a list without using the built-in sum() function. 

List = [ 1,2,3,4,5]
sum = 0
for num in List:
    sum += num
print(f'Sum of all Elements of the List {sum}')


# Intermediate List Questions 
#1. Identify and print the largest element present 
# in a list of numbers without using the built-in max() function. 
List = [ 12,34,5,67,33,1234]
Largest_Number = List[0]
for num in List:
    if num > Largest_Number:
        Largest_Number = num
print(f'Largest Number in the List is - {Largest_Number}')

# 2. Identify and print the smallest element present in a list of numbers 
# without using the built-in min() function. 

List = [ 12,34,5,67,33,1234]
Smallest_Number = List[0]
for num in List:
    if num < Smallest_Number:
        Smallest_NumberLargest_Number = num
print(f'Smallest Number in the List is - {Smallest_Number}')

# 3. Create a new list that contains the elements of the original list in reverse order,
#  without using the reverse() method or list slicing.

List = [1,2,3,4,5]
reversed_list = [ ]
for i in range (len(List)-1,-1,-1):
    reversed_list.append(List[i])
print(f'Original List {List}')
print(f'Reversed List {reversed_list}')

#5. Generate a new list from an original list, where all duplicate elements 
# have been removed, without using the built-in set() function. 

List = [ 1,2,3,4,5,2,3,4,5,6]
unique_list = [ ]
for item in List:
    if item not in unique_list:
        unique_list.append(item)
print(f'New List{unique_list}')
print(f'Old List{List}')

# 6. Write a boolean function that checks whether a specified element is contained within a given list.
List = [ 10,20,30,40,50,60,70]
element = 30
found = False
for item in List:
    if item == element:
        found = True 
        break 
print(f'Is item in the List- {found}')

# 7. Print only the elements from a list that are located at an index position which is an even number (0, 2, 4, ...). 
List = [ 1,2,3,4,5,6,7,8,9,10]
for i in range (len(List)-1):
    if(i%2 == 0):
        print(List[i], end = ' ')
    
print()

# 8. Print only the elements from a list that are located at an index position which is an odd number (1, 3, 5, ...). 
List = [ 1,2,3,4,5,6,7,8,9,10]
for i in range (len(List)):
    if(i%2 != 0):
        print(List[i], end = ' ')

print()

# 9. Iterate through a list of integers and separately count and print the total number 
# of even numbers and the total number of odd numbers. 

List = [1,2,3,4,5,6,7,8,9,10]
sum_even = 0 
sum_odd = 0
for num in List:
    if ( num % 2 == 0):
        sum_even += num
    else:
        sum_odd += num
print(f'Sum of Even Numbers - {sum_even}')
print(f'Sum of Odd numbers - {sum_odd}')

# 10. Given a list of numbers, create and print a second list where each element is the square of the 
# corresponding element in the original list. 

List = [ 1,2,3,4,5,6,7]
Square_list = [ ]
for num in List:
    Square_list.append(num**2)
print(f'Old List - {List}')
print(f'New List which do have Square Values from Old one - {Square_list}')

# 11. Combine the elements of two separate lists into a single new list without using the + or extend() operators. 
List1 = [1,2,3,4,5]
List2 = [6,7,8,9,10]
Combined_list = []
for num in List1:
    Combined_list.append(num)
for num in List2:
    Combined_list.append(num)
print(f'Old seperated List 1 - {List1}')
print(f'Old seperated List 2 - {List2}')
print(f'New Combined List  - {Combined_list}')

# 12. Modify a list in place so that all numbers less than zero (negative numbers) are removed. 
List = [ -1,-2,-44,-36,2,4,5,2,4]
positive_list = []
for num in List:
    if ( num >= 0 ):
        positive_list.append(num)
print(f'List with Positive Values Only -  {positive_list}')

# 13. Determine and print the second largest numerical value in a list without applying any sorting techniques. 
List = [  1,2,3,4,5,6,7,8,9]
Largest_num = List[0]
second_largest_number = None
for num in List:
    if( num > Largest_num):
        Largest_num = num
for num in List:
    if num!= Largest_num:
        if second_largest_number is None or num > second_largest_number:
            second_largest_number = num
print('Second Largest Number - ', second_largest_number)

# 14. Implement a cyclic shift operation on a list where every element is moved one position to the right,
#  and the last element wraps around to the first position. 
List = [ 1,2,3,4,5]
last_element = List[-1]
for i in range ( len(List)-1,0,-1):
    List[i]= List[i-1]
List[0]= last_element 
print(List)

#15. Write a function that returns True if a list is currently arranged in ascending order, and False otherwise. 
List = [ 1,10,3,4,5]
ascending = True 
for i in range ( len(List)-1):
    if List[i] > List[i+1]:
        ascending = False
        break
print(ascending)    

