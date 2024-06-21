
def dna_strand(dna: str) -> str:
    return dna.translate(str.maketrans("ATCG", "TAGC"))

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

if __name__ == "__main__":
    print(dna_strand("ATTGC"))  # Output: TAACG
    print(dna_strand("GTAT"))  # Output: CATA