## Using command line BLAST
---
### Assignment Instructions:
On your instructor's lab machine, there are two files in the subdirectory Bioinformatics_Spring_2023. The file “Rhizophagus_aa.gz” is the compressed file for predicted protein sequences of the fungus Rhizophagus irregularis, where “Rhizophagus_CDS.gz” contains the coding sequences for the species. Please first decompress these two files and create a BLAST-searchable database for protein sequences and coding sequences of this species, respectively.
From NCBI nucleotide and protein databases, please retrieve three nucleotide and protein sequences, respectively, of your favorite fungus. Save these sequences in multi-FASTA format and then transferred them to the lab machine (i.e., ip address 10.31.60.11).
Please perform blastn, blastp, tblastn searches using the two sequence files with default option values. Then perform searches by changing the following parameters:  
         
> Evalue threshold to 5, 1, 0.1, 0.001, 1e-10, 1e-20  
> Number of descriptions to 5, 2, 1  
> Number of alignments to 0  

---
### Steps:

1. I downloaded 3 protein sequnces from my favorite mushroom, [*Amanita muscaria*](https://en.wikipedia.org/wiki/Amanita_muscaria). 
