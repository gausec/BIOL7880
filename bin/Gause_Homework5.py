# Carol Gause
# Homework 5

# Specify the sequences to open from the command line
homework5_sequences = input("Type name of sequence file here, please: ")

# Create an outfile to save the sequences to
homework5_out = open('homework5_out.txt', 'w')


# Write the lines individually in the outfile
with open(homework5_sequences, 'r') as HW5Seq:
    for line in HW5Seq:
        homework5_out.write(line)


