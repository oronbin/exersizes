# ### exersize 1 - reverse each word of a string
# def reverse_word(str):
#     list =[]
#     lst = str.split()
#     for word in lst:
#         new_word= word[::-1]
#         list.append(new_word)
#     return ' '.join(list)
#
# string = 'hi my name is oron'
# print (reverse_word(string))


### exersize 3 - remove an intem from a list

# def remove_items(lst):
#     for i in lst:
#         if i >50:
#             lst.remove(i)
#     return lst
#
# list =[10,70,40,60]
# print(remove_items(list))


###exersize 4 - reverse dictionary mapping

# def rev_dic_mapping(dic):


###exersize 5 - display all duplicate items from a list

# def dis_dup(lst):
#     list = []
#     new_lst=[]
#     for num in lst:
#         if num not in list:
#             list.append(num)
#         else:
#             new_lst.append(num)
#     return new_lst
#
# lst= [10,20,60,30,20,60,40,30,70,80]
# print (dis_dup(lst))


### exersize 6 - filter dic to contain keys present in the given list

# def filter_dic_keys(dic,lst):
#     new_dic= dic.copy()
#     for elem in new_dic.keys():
#         if elem not in lst:
#             del dic[elem]
#     return dic
#
# d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# l1 = ['A', 'C', 'F']
#
# print (filter_dic_keys(d1,l1))


### exersize 7 - print the following number pattern

lst= ['1','2','3','4','5']
for i in range(1,6,-1):
    for elem in lst:
        a=elem*i
    print (a)
# print(lst[0]*5 \lst[1])ra