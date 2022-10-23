# converted_list = list(map(int,input().split()))
# print(converted_list)
# filter_list = [x for x in range(0, len(converted_list)+1, 2)]
# print(filter_list)

# converted_list = list(map(int,input().split()))
# print(converted_list)
# filter_list = [x for x in converted_list if converted_list.count(x) == 1]
# print(filter_list)

# a = [3*n+1 for n in range(10)]
# d = {}
# for idx, el in enumerate(a):
#     d.update({idx: el})
# print(d)

# a = open('data/text.txt', 'r')
# print(a)

# list = [1, 5, 2, 4, 6, 3, 7]
# print(list)
# for i in range(len(list)):
#     if list[i]<list[i+1]:
#         list.pop(i+1)
#         if list[i+1]>=list[i+2]:
#             list.pop(i + 1)
#             print(list)

# with open ('data/text.txt', 'r', encoding = 'utf-8') as data:
#     a = data.read().split()
#     a =list(map(int, a))
# print(a)
# for i in range(len(a)):
#     if a[i]+1 == a[i+1]:
#
#         # print(a[i]+1)