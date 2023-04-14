# Carol Gause
# Homework 4
# March 16, 2023
# Bioinformatics

# Setting my variables
Advisor="Susan McRae"
CoAdvisor="Christopher Balakrishan"
Me="Carol Gause"

# Altering the variables that I created and adding strings to print the message that I want
Name="Hello! My name is "+Me
Advisors=", and I work with Dr."+Advisor.split()[1]+" and Dr."+CoAdvisor.split()[1]
Interests=". I am interested in avian population genomics. Birds are cool!"

# Printing the message
print(Name+Advisors+Interests)
