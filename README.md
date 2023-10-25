# HW_5_Bioinformatic_functions

## Description
HW_5_Bioinformatic_functions is a collection of Python modules that provide a range of functionalities for bioinformatics tasks. These modules are designed to work with protein sequences, DNA/RNA sequences, and fastq files. They include functions to calculate molecular weight, transcribe DNA to RNA, filter and process fastq reads, and more.

## Modules

### run_protein_tool
The run_protein_tool module focuses on protein sequence analysis and offers the following functions:

- **molecular_weight**: Calculates the molecular weight of a protein sequence(s) in g/mol.
- **one_to_three_letter**: Converts 1-letter coded protein sequences to 3-letter coded sequences.
- **amino_acid_frequency**: Calculates the frequency of each unique amino acid in a protein sequence.
- **find_motifs**: Searches for a specified motif within a protein sequence.

### run_dna_rna_tools
The run_dna_rna_tools module is dedicated to DNA and RNA sequence manipulations. It includes functions for:

- **transcribe**: Transcribing DNA sequences into RNA by replacing T's with U's.
- **reverse**: Reversing the sequence.
- **complement**: Finding the complementary sequence for DNA or RNA.
- **reverse_complement**: Finding the reverse complementary sequence.

### filter_reads
The filter_reads module is designed for processing fastq files and offers the following functions:

- **gc_content(read)**: Calculates the GC composition of a read.
- **mean_quality**: Computes the average quality of a read on the phred33 scale.
- **gc_bounds_filter**: Filters reads based on GC composition.
- **length_bounds_filter**: Filters reads based on length.
- **quality_threshold_filter**: Filters reads based on average quality.

# HW_6_Bioinformatics Python Tools
This repository contains a set of Python functions for various bioinformatics tasks. These functions are designed to work with sequence data in formats such as FASTA, GenBank, and BLAST output. Here is an overview of the functions available in this toolset:

## Functions

1. **convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None)**
   - Converts a multiline FASTA file to a one-line FASTA file.

2. **select_genes_from_gbk_to_fasta(input_gbk, genes, n_before=1, n_after=1, output_fasta=None)**
   - Extracts gene sequences from a GenBank file based on specified gene names.
   - Allows selecting a specified number of genes before and after each occurrence of the gene of interest.

3. **change_fasta_start_pos(input_fasta, shift, output_fasta=None)**
   - Shifts the starting position of sequences in a one-line FASTA file by a specified number of positions.

4. **parse_blast_output(input_file, output_file=None)**
   - Parses BLAST output, extracts relevant information, and generates a more readable output.

### How to Use the Main Script

1. **Setup**: Ensure you have the necessary dependencies installed and the `scripts` directory contains the required module files.

2. **Run the Main Script**:
   - Execute the main script using Python.
   - This can be done from the command line or integrated into your own Python programs.

3. **Function Selection**:
   - The main script imports functions from various modules located in the `scripts` directory, specifically `dna_tools.py`, `fastq_tools.py`, `protein_tools_update.py`, and `bio_files_processor.py`.

4. **Function Execution**:
   - Inside the `main()` function, you can call the functions from the imported modules to perform specific tasks.
   - For example, `dna_tools()`, `fastq_tools()`, `protein_tools()`, and `bio_files_processor()` execute tasks related to DNA sequences, fastq file processing, protein sequences, and bio file processing, respectively.

5. **Run the Script**:
   - Execute the main script to perform the tasks you need.

## Troubleshooting

If you encounter any issues while using this toolkit, consider the following troubleshooting steps:

1. **Check Dependencies**: Ensure that you have all the required dependencies installed. The success of the toolkit's functions may depend on external libraries or modules.

2. **Verify Module Imports**: Double-check that you are correctly importing the required modules from the `scripts` directory. Make sure the module files exist and are accessible.

3. **Function Parameters**: Review the documentation for each function to ensure you are providing the correct parameters. Incorrect inputs may result in errors.

4. **Error Messages**: Pay attention to any error messages or exceptions that are raised. They can provide valuable information about what went wrong.

5. **Open an Issue**: If you encounter a persistent problem that you cannot resolve, consider opening an issue on the project's GitHub repository. Provide details about the issue, including the specific function you were using, the input data, and any error messages.

## Feedback

Your feedback is important for the improvement of this toolkit. If you have suggestions, feature requests, or any other feedback, please feel free to reach out. You can provide feedback through the following channels:

- Open an issue on the project's GitHub repository to report bugs or request features.
- Send an email to the project's author to provide feedback or ask questions.




