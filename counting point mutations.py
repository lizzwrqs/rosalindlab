with open("rosalind_hamm.txt", "r", encoding="utf-8") as file:
    line = file.read().strip().split("\n")
l1 = line[0]
l2 = line[1]
razniebukvi = 0
for i in range(len(l1)):
    if l1[i] != l2[i]:
        razniebukvi += 1
print(razniebukvi)