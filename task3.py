# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

list1 = [1, 2, 4, 6, 2, 1]

list2 = list(set(list1))
print(list2)


# ===============

# list_1 = [1, 3, 6, 1, 7, 4, 3]
# list_2 = {}
# print(list_1)
# for i in list_1:
#         if not i in list_2:
#                 list_2[i] = 0
#         list_2[i] += 1

# list_3 = []
# for i in list_2:
#         if list_2[i] == 1:
#                 list_3.append(i)

# print(list_3)