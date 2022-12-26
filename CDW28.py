def DNA_strand(dna):
    output = ''
    for c in dna:
        if c == 'A':
            output += 'T'
        if c == 'T':
            output += 'A'
        if c == 'C':
            output += 'G'
        if c == 'G':
            output += 'C'
    return output


print(DNA_strand('ATTGC'))

#pairs = {'A':'T','T':'A','C':'G','G':'C'}
#def DNA_strand(dna):
#    return ''.join([pairs[x] for x in dna])