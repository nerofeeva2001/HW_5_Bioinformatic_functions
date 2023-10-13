def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    if output_fasta is None:
        output_fasta = f"{input_fasta}.fasta"
    
    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        for record in SeqIO.parse(infile, "fasta"):
            outfile.write(f">{record.id}\n{record.seq}\n")

def select_genes_from_gbk_to_fasta(input_gbk, genes, n_before=1, n_after=1, output_fasta=None):
    # Implement this function to extract genes from a GBK file and create a FASTA file.

def change_fasta_start_pos(input_fasta, shift, output_fasta=None):
    if output_fasta is None:
        output_fasta = f"{input_fasta}.fasta"
    
    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        for record in SeqIO.parse(infile, "fasta"):
            sequence = record.seq
            shifted_sequence = sequence[shift:] + sequence[:shift]
            outfile.write(f">{record.id}\n{shifted_sequence}\n")

def parse_blast_output(input_file, output_file=None):
    if output_file is None:
        output_file = "parsed_blast_results.txt"

    results = []

    with open(input_file, "r") as infile:
        lines = infile.read().split("Sequences producing significant alignments:")
        for line in lines[1:]:
            lines = line.split("\n")
            query_line = lines[0].strip()
            description = lines[1].strip().split("Description: ")[1]
            results.append((query_line, description))

    results.sort(key=lambda x: x[1])  # Sort by description

    with open(output_file, "w") as outfile:
        for query_line, description in results:
            outfile.write(f"{query_line}\n{description}\n\n")