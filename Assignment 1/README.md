# Assignment1

## Description
This assignment consists of several modules that perform different tasks related to running process their instance and some basic code.

### Ques 1:
- Write a program to return below output from given input (with and without uses of inbuilt function)
Input -  "My name is Suraj"
output - "Suraj is name My"

### 1.(i). reverse_string.py
This script reverses a given string while maintaining the order of words within the string. It splits the string into words, reverses each word individually, and then joins them back together to form the reversed string.

### 1.(ii). reverse_sentence.py
The reverse_sentence.py script reverses the order of words in a sentence. It splits the sentence into individual words, reverses the order of the words, and then joins them back together to form the reversed sentence.

### Ques 2:
- Write a program to monitor the applications running on your system. 
To test: Execute any application like browser, notepad, calculator etc and make sure 
that not more than 2 instances of the same application can be running.

### 2. count_running_instances.py
count_running_instances.py counts the number of running instances of specified processes. It utilizes the psutil library to iterate through running processes and count instances of each specified process name.

### Ques 3:
- Write a Program 
1. to find all the list of all running process in your System
2. Display the count of each running process.
3. Store this information in a CSV File.

### 3. save_process_counts_to_csv.py
This script gets the count of each running process and saves the information to a CSV file. It utilizes the psutil library to retrieve process information and the csv module to write the data to a CSV file.

### Ques 4: I. Given a String of Characters
1. Print the three most common characters along with their occurrence count.
2. Sort in descending order of occurrence count.
3. If the occurrence count is the same for any character, sort the characters in alphabetical order.
Final Output. 
Top 3 Characters based on the above critera
E.g. 
Input: HAPPIESTMINDS
Output : 
I: 2
P: 2
S: 2

### 4. most_common_characters.py
most_common_characters.py finds and prints the top three most common characters in a given string. It counts the occurrences of each character in the string, sorts them based on frequency, and prints the top three most common characters along with their counts.

### Ques 5:
- Write a program to print fibonacci series for the given input occurence (if user gives i\p as 6 then it should print series till 6th number)
FiBoNACCI series
0 1 1 2 3 5 8 13 21
 
Input: 6, Output: 0 1 1 2 3 5
Input: 10, Output: 0 1 1 2 3 5 8 12 21 34

### 5. fibonacci.py
fibonacci.py generates a Fibonacci sequence up to the nth number. It calculates the Fibonacci sequence using a loop and returns a list containing the sequence.

## Usage
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the code snippets.
3. Run each script individually by executing `python script_name.py`.
4. Follow the prompts or provide necessary input when prompted.

## Dependencies
- Python 3.x
- psutil (install via `pip install psutil`)
Feel free to explore the code snippets and use them as examples or templates for your own projects!