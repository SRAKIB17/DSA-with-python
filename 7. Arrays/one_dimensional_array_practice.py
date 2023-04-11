from array import *
# 1. create an array and traverse
my_arr = array('i', [1, 2, 3, 4, 5])

# # traverse an array
# for i in my_arr:
#     print(i)

# 2. Access individual  element by index
# print(my_arr[0])


# 3. Remove any array element using remove method() method:
# my_arr.remove(value)
# my_arr.remove(1)


# 5. Remove last array element using pop() method
# print(my_arr.pop(0)) # 5
# # my_arr.pop(index)
# print(my_arr)

# 6. Reverse a python array using reverse() method
my_arr.reverse()
print(my_arr)

# 7. Get array buffer information through buffer_info() method.
print(my_arr.buffer_info())

# 8. Check for number of occurrences of an element using count() method
print(my_arr.count(10))
# 9. Convert array to string using tobytes() method
print(my_arr.tobytes())

# 10. slicing array
