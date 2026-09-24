with open("rosalind_gc.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
namendna = {}
nameseq = ""
for l in lines:
    l = l.strip()
    if l.startswith(">"):
        nameseq = l[1:]
        namendna[nameseq] = ""
    else:
        namendna[nameseq] = namendna[nameseq] + l
topname = ""
topgc = 0.0
for name, dna in namendna.items():
    g = dna.count("G")
    c = dna.count("C")
    gcpercent = (g + c) / len(dna) * 100
    if gcpercent > topgc:
        topgc = gcpercent
        topname = name
print(topname)
print(topgc)