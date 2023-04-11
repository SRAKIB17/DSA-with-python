# time efficient
from array import *
arr1 = array('i',[1,2,3,4,5,6])
# print(arr1)

# def searchInArray(array=object, value=str):
#     for i in array: #O(n)
#         if(i==value): #O(1)
#             return array.index(value) #O(n)
#     return "the element dose not exist" #O(n)
# # Time Complexity: O(n)
# print(searchInArray(array=arr1, value=0))

# def binary_search(list, find_value):
#     low = 0
#     high=len(list)
#     while low<=high:
#         mid = (low+high)//2
#         if(list[mid]<find_value):
#             low = mid        
#         elif list[mid] >find_value:
#             high = mid
#         else:
#             return mid
#         return mid

# x = binary_search(arr1, 10)
# print(x)