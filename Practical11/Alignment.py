seq1 = "MLSRAVCGT"
seq2 = "MLCRAACST"
edit_distance = 0  # set initial distance as zero
for i in range(len(seq1)):  # compare each amino acid
    if seq1[i] != seq2[i]:
        edit_distance += 1  # add a score 1	if amino acids are different
print(edit_distance)
