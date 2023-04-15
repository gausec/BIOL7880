## Assignment 1: Creating Directories, Navigating File Systems, and Archiving Files in Bash Shell

### Overview:  
This assignment involved performing various tasks using a Linux terminal. These included:
- Creating a subdirectory within the home directory
- Navigating directories
- Creating and modifying files
- Changing file permissions
- Creating archive files using the `tar` command. 

The final requirement of assignment 1 involved describing the findings & results of the tasks in a text file, and then storing it in a tar file (located in results directory of this repository). 

---
### Assignment Instructions:  
1. Within the home directory, create a subdirectory and name it as “yourlastname_firstname”. Now you should have a subdirectory for yourself.
2. Next, go to your newly created directory, create another subdirectory “HW1”. Please follow the same format for your other future homework assignments (e.g., HW1, HW2, HW3 …).
3. Do the following: 
> Use `pwd` command to find the path of your current working directory.  
> Go to “HW1”, now type `ls –l`, what did you see?  
> Next , type `ls –al`, what did you see? Were they directories or files? Please explain.  
> Next, type `cd .`. What is your current working directory?  
> Next, type `cd ..`, find your current working directory. What is the path of your current directory?  
> Next, go back to your HW1 and create a file “HW1_answer” using `vi`, and explain your finding from above operations.  
4. Create another file “about_me” using `vi`. Please describe yourself (e.g., your department, advisor, research interest, your previous bioinformatics experience etc.).
5. Change the permission mode of your “about_me” file to `rwxrw----` (i.e., owner can read, write and execute; group member can read, write, but not execute; other people cannot do anything with this file).
6. Use `cd` to go back to your home directory. Use `tar` to create an archive file for your subdirectory.

---
### Steps:

1. Connect to remote server using `ssh` command
```
ssh bioinfo@ipaddress 
```

2. Navigate to the spring 2023 course directory and create a new subdirectory for my work and for homework assignment 1
```
cd Bioinformatics_Spring_2023
```
```
mkdir Gause_Carol
```
```
cd Gause_Carol
```
```
mkdir HW1
```
```
cd HW1
```
3. Type the commands listed in step 3 of the instructions
4. Create a text file
```
vi about_me
```
*This will open the vi editor with a new file named "about_me".*

5. Press `i` to enter insert mode and press "Esc" to exit insert mode. Save changes with `:wq` and press enter. 
6. Change permissions of the file
```
chmod u=rwx,g=rw-,o=---, about_me
```
7. Create an archive file of my directory
```
cd ..
```
```
tar -cvf Homework1.tar HW1
```

