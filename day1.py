from collections import Counter
list1=list()
list2=list()
lines=[]
with open('day1.txt') as file:
    lines=file.read().splitlines()
for i in range(len(lines)):
    list1.append(int(lines[i].split(" ")[0]))
    list2.append(int(lines[i].split(" ")[-1]))
list1.sort()
list2.sort()
#pat1
total=0

for i in range(len(list1)):
    total+=abs(list1[i]-list2[i])
print(total)
#part2
counts = Counter(list2)
similarity_score = 0
for num in list1:
    similarity_score += num * counts[num]
print(similarity_score)

