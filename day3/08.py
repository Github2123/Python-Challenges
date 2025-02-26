dna_sequence = ['A', 'T', 'G', 'C', 'A']
x={'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
complementry_strand=[x[base] for base in dna_sequence]
print(complementry_strand)
