# **HW_5_Bioinformatic_functions**
## *run_protein_tool*
### The following functions are implemented:
        
        molecular_weight This function takes 1-letter coded protein sequence(s) (string) and calculates molecular weight rounded to integer in g/mol. The function is not case-sensitive. 
        
        one_to_three_letter This function takes 1-letter coded protein sequence(s) (string) and returns a 3-letter coded sequence(s) without spaces (string). 
        
        amino_acid_frequency This function takes 1-letter coded protein sequence(s) (string), calculates frequency for each unique amino acid and creates a dictionary with amino acids as keys and corresponding frequencies as values. 
        
        find_motifs This function takes two string arguments: 1-letter coded protein sequence(s) and a motif of interest, where motif is any sequence which occurence will be searched for in the input protein sequence(s). The function returns position(s) of the       motif. If a motif was not found, the function will return an empty list. Please note that this function can only search for one motif at a time. 


## *run_dna_rna_tools* 
### The following functions are implemented:
        transcribe - Function for transcribing DNA into RNA (replaces all T's with U's)
        
        reverse - Function to reverse the sequence (uses a negative step cut)
        
        complement - Function for finding a complementary sequence (creates a dictionary with pairs of complementary nucleotides, initializes an empty string for the complementary sequence, goes through each symbol in the original sequence, if the symbol is in the dictionary, adds its complementary nucleotide to the result, otherwise, adds the symbol unchanged)
        
        reverse_complement - Function for finding the reverse complementary sequence (finds the complementary sequence and reverses it)

## *filter_reads*
### The following functions are implemented:

        gc_content(read) - Function for calculating GC composition of the reed
        
        mean_quality - Function for calculating the average quality of a reid on the phred33 scale

        gc_bounds_filter - Function for filtering reids by GC composition
        
        length_bounds_filter - Function for filtering reids by length

        quality_threshold_filter - Function for filtering reids by average quality


