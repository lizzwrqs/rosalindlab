with open("rosalind_iprb.txt", "r", encoding="utf-8") as file:
    line = file.read().split()
AA = int(line[0])
Aa = int(line[1])
aa = int(line[2])
all = AA + Aa + aa
pAaxAa = (Aa / all) * ((Aa - 1) / (all - 1))
pAaxaa = 2 * (Aa / all) * (aa / (all - 1))
paaxaa = (aa / all) * ((aa - 1) / (all - 1))
paa = pAaxAa * 0.25 + pAaxaa * 0.5 + paaxaa * 1
pAAandaa = 1 - paa
print(pAAandaa)