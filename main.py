from Bio.Seq import Seq
import re
import subprocess

# IUPAC nucleotide code
iupac = ['A', 'C', 'G', 'T', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N', 'I', '.', '-']

# if statement seeing whether the input file type is correct
while True:
    # Ask for user input file
    input_seqs = input("Enter path to MitoGenome input file: ")
    if not input_seqs.lower().endswith(('.fasta', '.fasta.gz', '.fasta.bz2', '.fasta.xz', '.fastq', '.fastq.gz',
                                        '.fastq.bz2', '.fastq.xz')):
        print("Incompatible file format. \nOnly .fasta, and .fastq files are supported.\n"
              "Compressed versions of the aforementioned file types are also accepted in .gz, .bz2, and .xz formats.")
        continue
    else:
        break

while True:
    # Ask for user output file
    output_seqs = input("Enter path to MitoGenome output file: ")
    if not output_seqs.lower().endswith(('.fasta', '.fasta.gz', '.fasta.bz2', '.fasta.xz', '.fastq', '.fastq.gz',
                                        '.fastq.bz2', '.fastq.xz')):
        print("Incompatible file format. \nOnly .fasta, and .fastq files are supported.\n"
              "Compressed versions of the aforementioned file types are also accepted in .gz, .bz2, and .xz formats.")
        continue
    else:
        break

# While loop continues to ask user to input their forward primer if an
# incorrect value is entered based on IUPAC genetic code (plus I)
while True:
    f_primer = input("Enter 5' primer sequence: ").upper()
    if not all([x in iupac for x in f_primer]):
        print("Please enter a valid IUPAC sequence")
        continue
    elif re.search("I", f_primer):
        f_primer = re.sub("I", "N", f_primer)
        break
    else:
        break

# While loop continues to ask user to input their reverse primer if an
# incorrect value is entered based on IUPAC genetic code (plus I)
while True:
    # Ask user to input their reverse primer
    r_primer = input("Enter 3' primer sequence: ").upper()
    if not all([x in iupac for x in r_primer]):
        print("Please enter a valid IUPAC sequence")
        continue
    elif re.search("I", r_primer):
        r_primer = re.sub("I", "N", r_primer)
        break
    else:
        break
# Ask user input for Min and max loci lengths
while True:
    try:
        min_loci, max_loci = input("Enter the minimum and maximum range for loci lengths separated by a space: ").split()
        int(min_loci)
        int(max_loci)
        if max_loci < min_loci:
            print("Invalid entry. Max length < min length.")
            continue
        else:
            break
    except ValueError:
        print("Invalid entry. Please enter a numeric values.")

# Converts the 3' adapter to a Seq data type and stores in variable seq
seq = Seq(r_primer)
# runs the complement() method on seq variable and stores as comp_r_primer
comp_r_primer = seq.complement()
# concatenates 5' and 3' adapters and converts to string and stores in variable
# that is passed to the cutadapt module
link_adapter = str(f_primer + '...' + comp_r_primer)

# Passes the user input to the cutadapt program through the subprocess module
# Sucessful run will return the specified output, info.tsv, and untrimmed.fasta files
subprocess.run(['cutadapt', '-g', link_adapter, '-e', '0.2', '--cores=0', '--info-file=info.tsv', '-m', min_loci,
                '--too-short-output', 'short_seqs.fasta', '-M', max_loci, '--too-long-output', 'long_seqs.fasta',
                '--untrimmed-output', 'untrimmed.fasta', '-o', output_seqs, input_seqs])

print("Trimming Complete")
