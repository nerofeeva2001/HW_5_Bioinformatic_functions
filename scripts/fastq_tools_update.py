def gc_content(read):
    gc_count = 0
    for base in read:
        if base in "GCgc":
            gc_count += 1
    return gc_count / len(read) * 100

def mean_quality(quality):
    total_score = 0
    for char in quality:
        score = ord(char) - 33
        total_score += score
    return total_score / len(quality)

def read_fastq_file(input_path):
    seqs = {}
    with open(input_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            name = lines[i].strip()
            sequence = lines[i + 1].strip()
            quality = lines[i + 3].strip()
            seqs[name] = (sequence, quality)
            i += 4
    return seqs

def write_filtered_fastq(filtered_seqs, output_filename):
    with open(f'fastq_filtrator_results/{output_filename}.fastq', 'w') as output_file:
        for name, (sequence, quality) in filtered_seqs.items():
            output_file.write(f"{name}\n{sequence}\n+\n{quality}\n")

def filter_reads(input_path, output_filename, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
    seqs = read_fastq_file(input_path)
    filtered_seqs = {}

    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)
    
    for name, (read, quality) in seqs.items():
        if gc_bounds[0] <= gc_content(read) <= gc_bounds[1] and length_bounds[0] <= len(read) <= length_bounds[1] and mean_quality(quality) >= quality_threshold:
            filtered_seqs[name] = (read, quality)

    write_filtered_fastq(filtered_seqs, output_filename)




