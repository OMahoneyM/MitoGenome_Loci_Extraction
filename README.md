A simple python script to create reference libraries of specific loci from whole and partial mitochondrial genomes

---

## Requirements
In order to run this script you should first create a conda environment and install `Biopython` as well as `Cutadapt`.
- If you do not have a version of Anaconda install on your machine you can find the instructions and download [here](https://docs.anaconda.com/anaconda/install/index.html).
- You can learn more about the packages at their documentation pages below:
  - [Biopython](https://biopython.org/)
  - [Cutadapt](https://cutadapt.readthedocs.io/en/stable/)


To set up a conda environment open terminal and type:
```commandline
conda create --name MitoGenEx python=3.9
``` 
Activate the newly created environment:
```commandline
source activate MitoGenEx
```
Install the `Biopython` package in the `MitoGenEx` environment:
```commandline
conda install biopython
```
Install `Cutadapt` in the environment:
```commandline
conda install cutadapt
```
Navigate to the directory where the python script is downloaded, run it, then follow the prompts.

## Running the Script
The **first prompt** will ask you to input the location of the fasta file containing the mitogenomes you would like trimmed. If your file is not in the same directory as the script, you will need to specify its absolute path. That should look something like this in macOS: 
```commandline
/Users/ExampleUser/Documents/DataDirectory/Example.fasta
```

The **second prompt** will ask you to name your output. Again you should specify the aboslute path unless you want your output in the same directory as the script.
- The only inputs/outputs that `Cutadapt` accepts are `.fasta` and `.fastq` as uncompressed files or compressed as `.gz`, `.bz2`, and `.xz`. 

The **third prompt** will ask you to enter the 5' adapter sequence.

The **fourth prompt** will ask you to enter the 3' adapter sequence.
- The adapter sequences must follow the IUPAC genetic code or else it will fail. The one exception is Inosine, **I**,  which will be converted to **N** before processing. 

The **fifth prompt** will ask you to enter the minimum and maximum range of loci lengths (in basepairs) for your target loci. These values should be entered together on the same line with a space between them.
```commandline
% 650 680
```
- Please note that the minimum value is entered first, followed by the maximum.

If no prompts return an error asking you to reinput the above data in the correct format, then the script will pass those values to `Cutadapt`, which will begin to output information to the console. 

When complete the directory you specified for you output should contain the five files below:
- **output file**
  - File containing the sequences that were successfully trimmed 
- **info.tsv**
  - File containing detailed information about where adapters were found in each read
- **short_seqs.fasta**
  - File containing the sequences that are too short according to the minimum length value
- **long_seqs.fasta**
  - File containing the sequences that are too long according to the maximum length value
- **untrimmed.fasta**
  - File containing the sequences that the adapters did not recognize and therefore could not trim