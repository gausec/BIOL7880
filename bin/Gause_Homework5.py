# Carol Gause
# Homework 5


# Import sys module to allow access to command line arguments & set the variable 'file' to the first command line argument (name of input file)
import sys
file=sys.argv[1]


# Open input file in read/write mode & create a new output file in read/write mode with the '.txt' extension
fp1 = open(file, 'r')
fp2 = open(file+'.txt', 'w+')


# Read lines of the input file and store as a list of strings
HW5seq=fp1.readlines()


# Iterate through each line in the list of input file lines 
    
for line in HW5seq:
    if line[0]=='>':                        # Write only the first element of the line (the sequence ID) followed by a new line if the first character is a '>'
        fp2.write(line.split()[0]+'\n')
    else:                                   # Otherwise write entire line to output file
        fp2.write(line)

        
# Close the files        
fp1.close()
fp2.close()

        
