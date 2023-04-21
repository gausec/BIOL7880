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
---

### Writing the script:

1. Create a new python script
```
nano Gause_Homework5.py
```

2. Import sys module to allow access to command line arguments & set the variable 'file' to the first command line argument (name of input file)
```
import sys
file=sys.argv[1]
```

3. Open input file in read mode & create a new output file in read/write mode with the '.txt' extension
```
fp1 = open(file, 'r')
fp2 = open(file+'.txt', 'w+')
```

4. Read lines of the input file and store as a list of strings
```
HW5seq=fp1.readlines()
```

5. Iterate through each line in the list of input file lines 
``` 
for line in HW5seq:
    if line[0]=='>':                        # Write only the first element of the line (the sequence ID) followed by a new line if the first character is a '>'
        fp2.write(line.split()[0]+'\n')
    else:                                   # Otherwise write entire line to output file
        fp2.write(line)
```
        
6. Close the files        
```
fp1.close()
fp2.close()
```
---

### Copying my outfile to my local computer

1. Use `scp` command to copy my outfile to my local computer in the current working directory 
```
scp <username>@<ipaddress>:/Users/bioinfo/Bioinformatics_Spring_2023/Gause_Carol/HW5/homework5_out.txt .
```
