# Python program to remove all adjacent duplicates from a string

# Recursively removes adjacent duplicates from str and returns
# new string. las_removed is a pointer to last_removed character
# def removeUtil(string, last_removed):
#     # If length of string is 1 or 0
#     if len(string) == 0 or len(string) == 1:
#         return string
#
#         # Remove leftmost same characters and recur for remaining
#     # string
#     if string[0] == string[1]:
#         last_removed = ord(string[0])
#         while len(string) > 1 and string[0] == string[1]:
#             string = string[1:]
#         string = string[1:]
#
#         return removeUtil(string, last_removed)
#
#         # At this point, the first character is definiotely different
#     # from its adjacent. Ignore first character and recursively
#     # remove characters from remaining string
#     rem_str = removeUtil(string[1:], last_removed)
#
#     # Check if the first character of the rem_string matches
#     # with the first character of the original string
#     if len(rem_str) != 0 and rem_str[0] == string[0]:
#         last_removed = ord(string[0])
#         return (rem_str[1:])
#
#         # If remaining string becomes empty and last removed character
#     # is same as first character of original string. This is needed
#     # for a string like "acbbcddc"
#     if len(rem_str) == 0 and last_removed == ord(string[0]):
#         return rem_str
#
#         # If the two first characters of str and rem_str don't match,
#     # append first character of str before the first character of
#     # rem_str.
#     return ([string[0]] + rem_str)
#
#
# def remove(string):
#     last_removed = 0
#     return toString(removeUtil(toList(string), last_removed))
#
#
# # Utility functions
# def toList(string):
#     x = []
#     for i in string:
#         x.append(i)
#     return x
#
#
# def toString(x):
#     return ''.join(x)
#
#
# # Driver program
# string1 = "geeksforgeeg"
# print(remove(string1))
#
# string2 = "azxxxzy"
# print(remove(string2))
#
# string3 = "caaabbbaac"
# print(remove(string3))
#
# string4 = "gghhg"
# print(remove(string4))
#
# string5 = "aaaacddddcappp"
# print(remove(string5))
#
# string6 = "aaaaaaaaaa"
# print(remove(string6))
#
# string7 = "qpaaaaadaaaaadprq"
# print(remove(string7))
#
# string8 = "acaaabbbacdddd"
# print(remove(string8))
#
# string9 = "acbbcddc"
# print(remove(string9))
#
# string10 = "mississipie"
# print(remove(string10))
# def removeDuplicates(str,k):
#     if(k >= len(str)-1):
#         return str
#
#     for i in range(0,len(str)-1):
#         if(str[i]==str[i+1]):
#             j=i
#             while(j < len(str)-1):
#                 if(str[j] != str[j+1]):
#                     break
#                 j += 1
#             if(j+1 < len(str)):
#                 str = str[:i]+str[j+1:]
#                 return removeDuplicates(str, i)
#             elif(j+1 == len(str)):
#                 str = str[:i]
#                 return str
#     return str
#
#
# n = 1
# for testcase in range(0,n):
#     mystr = "mississipie"
#     print(removeDuplicates(mystr,0))