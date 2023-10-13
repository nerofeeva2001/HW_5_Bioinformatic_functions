# **HW_5_Bioinformatic_functions**
## *run_protein_tool*
is a Python module that allows you to perform various procedures on proteins
### The following functions are implemented:
        
        molecular_weight This function takes 1-letter coded protein sequence(s) (string) and calculates molecular weight rounded to integer in g/mol. The function is not case-sensitive. 
        
        one_to_three_letter This function takes 1-letter coded protein sequence(s) (string) and returns a 3-letter coded sequence(s) without spaces (string). 
        
        amino_acid_frequency This function takes 1-letter coded protein sequence(s) (string), calculates frequency for each unique amino acid and creates a dictionary with amino acids as keys and corresponding frequencies as values. 
        
        find_motifs This function takes two string arguments: 1-letter coded protein sequence(s) and a motif of interest, where motif is any sequence which occurence will be searched for in the input protein sequence(s). The function returns position(s) of the       motif. If a motif was not found, the function will return an empty list. Please note that this function can only search for one motif at a time. 


## *run_dna_rna_tools* 
is a Python module that allows you to perform various procedures on DNA or RNA sequences
### The following functions are implemented:
        transcribe - Function for transcribing DNA into RNA (replaces all T's with U's)
        
        reverse - Function to reverse the sequence (uses a negative step cut)
        
        complement - Function for finding a complementary sequence (creates a dictionary with pairs of complementary nucleotides, initializes an empty string for the complementary sequence, goes through each symbol in the original sequence, if the symbol is in the dictionary, adds its complementary nucleotide to the result, otherwise, adds the symbol unchanged)
        
        reverse_complement - Function for finding the reverse complementary sequence (finds the complementary sequence and reverses it)

## *filter_reads*
is a Python module that allows you to perform various procedures on fastq-files
### The following functions are implemented:

        gc_content(read) - Function for calculating GC composition of the reed
        
        mean_quality - Function for calculating the average quality of a reid on the phred33 scale

        gc_bounds_filter - Function for filtering reids by GC composition
        
        length_bounds_filter - Function for filtering reids by length

        quality_threshold_filter - Function for filtering reids by average quality


# **HW_6_ioinformatics Python Tools** 
This repository contains a set of Python functions for various bioinformatics tasks. These functions are designed to work with sequence data in formats such as FASTA, GenBank, and BLAST output. Here is an overview of the functions available in this toolset:

## Functions
1. convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None)
This function takes a multiline FASTA file as input and converts it to a one-line FASTA file. If the output_fasta parameter is not provided, it will generate an output file with the same name as the input file but with the ".fasta" extension.

2. select_genes_from_gbk_to_fasta(input_gbk, genes, n_before=1, n_after=1, output_fasta=None)
This function extracts gene sequences from a GenBank file based on the specified gene names. It allows you to select a specified number of genes before and after each occurrence of the gene of interest. If the output_fasta parameter is not provided, it will generate an output file with the same name as the input file but with the ".fasta" extension.

3. change_fasta_start_pos(input_fasta, shift, output_fasta=None)
This function shifts the starting position of sequences in a one-line FASTA file. It takes an integer shift that determines how many positions to shift the sequence and creates an output file. If the output_fasta parameter is not provided, it will generate an output file with the "_shifted.fasta" extension.

4. parse_blast_output(input_file, output_file=None)
This function parses BLAST output, extracts relevant information, and generates a more readable output. It reads the BLAST output file and extracts the query lines and their descriptions. The results are then sorted by description and saved to an output file. If the output_file parameter is not provided, it will create an output file named "parsed_blast_results.txt."
