# HW_5_Bioinformatic_functions
##run_protein_tool

The following functions are implemented:

molecular_weight This function takes 1-letter coded protein sequence(s) (string) and calculates molecular weight rounded to integer in g/mol. The function is not case-sensitive. 
one_to_three_letter This function takes 1-letter coded protein sequence(s) (string) and returns a 3-letter coded sequence(s) without spaces (string). 
amino_acid_frequency This function takes 1-letter coded protein sequence(s) (string), calculates frequency for each unique amino acid and creates a dictionary with amino acids as keys and corresponding frequencies as values. 
find_motifs This function takes two string arguments: 1-letter coded protein sequence(s) and a motif of interest, where motif is any sequence which occurence will be searched for in the input protein sequence(s). The function returns position(s) of the motif. If a motif was not found, the function will return an empty list. Please note that this function can only search for one motif at a time. 

