L1 = ["1", "2", "2", "5", "3", "2", "5", "2", "4", "3"]


counts = {}
# list1 = []
for num in L1:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

uniquee = [num for num in counts if counts[num] == 1]

print(uniquee)

# list1 = []
# for i in L1:
#     if L1.count(i) == 1:
#         list1.append(i)
# print(list1) 


# list1 = []
# for num in counts:
#     if counts[num] == 1:
#         list1.append(num)
# print(list1) 

# uniquee = [num for num in counts if counts[num] == 1]

# print(uniquee)

