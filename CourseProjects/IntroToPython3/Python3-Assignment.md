# Intro to writing Python3 scripts and creating variables in the command line

## Instructions:
In Bioinformatics_Spring_2023 on the lab machine, please create a subdirectory using your lastname_firstname. Then under this subdirectory, please create a subdirectory “HW4”.

Under your own "HW4" subdirectory, write a python script “homework4.py”. In that script, please create two variables for the full names of yourself and your major professor, respectively. Your script should call the two variables to print a short introduction about yourself in the following format:
```
          My name is xxx (use string concatenation here and call variable myself to

                 write your name).

        I am interested in xxxxx.

          I worked with Dr. xxx (Please use string built-in function split() to retrieve your professor’s last name here from the variable myadvisor).
```
---

## Steps

1. Making my new subdirectory
```
cd Bioinformatics_Spring_2023
mkdir Gause_Carol
cd Gause_Carol
mkdir HW4
cd HW4
```
2. Writing the script (I am annotating my script as I go)
```
nano homework4.py
```

3. Setting my variables
```
Advisor="Susan McRae"
CoAdvisor="Christopher Balakrishan"
Me="Carol Gause"
```

4. Altering the variables that I created and adding strings to print the message that I want
```
Name="Hello! My name is "+Me
Advisors=", and I work with Dr."+Advisor.split()[1]+" and Dr."+CoAdvisor.split()[1]
Interests=". I am interested in avian population genomics. Birds are cool!"
```


5. Printing the message
```
print(Name+Advisors+Interests)
```

6. Save and run script
```
ctrl^x #exit
y # yes, save
enter #confirm script name as homework4.py

Python3 homework4.py
```

7. Save script output to a text file
```
python3 homework4.py > homework4.txt
```
