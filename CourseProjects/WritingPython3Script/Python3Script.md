### **Instructions:**
In Bioinformatics_Spring_2023 on the lab computer, there is a file called “homework5_sequences”. Please create a subdirectory "HW5" under your own subdirectory, and copy “homework5_sequences” into your "HW" subdirectory.

Write a short python script “My_lastname_homework5.py” to retrieve the accession numbers and sequences from the input file. Please read the input file name from the command lines. Your script should be executed like the following:

          python  name_homework5.py   homework5_sequences

Please write your output file as “homework5_out”. The output file should contain the following information and be in the following format:

>Accession number 1

   Sequence 1

>Accession number 2

   Sequence 2

>Accession number 3

Here accession numbers and sequences should be the originals from the input file “homework5_sequences”.

---


### Creating the new directory and transfering the homework5_sequences file from my local machine to the remote lab server

1. From remote lab server, create a new subdirectory
```
mkdir HW5
```
2. Use `scp` from my local machine to copy the homework5_sequences file into my working directory on the remote server
```
scp /Users/Carol/Documents/homework5_sequences <username>@<ipaddress>:/Users/bioinfo/Bioinformatics_Spring_2023/Gause_Carol/HW5
```


### Writing the script:

1. Specify the sequences to open from the command line via user input
```
homework5_sequences = input("Type name of sequence file here, please: ")
```

2. Create an outfile where the sequences will go
```
homework5_out = open('homework5_out.txt', 'w')
```

3. Write the lines individually in the outfile. In the with statement, each line of the input file is read using a for loop, and the contents of each line are written to the output file using the write() method.

```
with open(homework5_sequences, 'r') as HW5Seq:
    for line in HW5Seq:
        homework5_out.write(line)
```

### Copying my outfile to my local computer

1. Use `scp` command to copy my outfile to my local computer in the current working directory 
```
scp <username>@<ipaddress>:/Users/bioinfo/Bioinformatics_Spring_2023/Gause_Carol/HW5/homework5_out.txt .
```
