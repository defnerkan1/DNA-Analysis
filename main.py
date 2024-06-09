# sample DNA of the criminal
sample = ['GTA','GGG','CAC']

# read the DNA of each suspect
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data

# take a DNA string and split it into a list of codons
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i+3) < len(dna):
      codons.append(dna[i:i+3])     
  return codons

# check how many of a suspect's codons match the sample codons
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

# decide on the identity of the criminal
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)

  if num_matches >= 3:
    print " %s of matches found. Continue investigation." % num_matches
  else:
    print"%s of matches found. The suspect can be freed." % num_matches

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")  
