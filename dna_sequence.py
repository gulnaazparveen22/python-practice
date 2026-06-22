dna = "ATGCGATCGGCTA"

length = len(dna)

gc_count = dna.count("G") + dna.count("C")
gc_content = (gc_count / length) * 100

print("DNA Sequence:", dna)
print("Length:", length)
print("GC Content:", gc_content)