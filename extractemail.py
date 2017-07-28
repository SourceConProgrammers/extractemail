import re
import csv


def main():
    # We define a variable to save the file path.
    # './' means the same folder directory. class_1_hw_1.txt is the file you should
    # download from this link: https://drive.google.com/open?id=0B8JmvhAPvuBYWFFSSlF6X0luX0E
    filepath = "./class_1_hw_1.txt"
    output = "./class_1_hw_1_emails.csv"
    # This will open the csv file in write mode. The '+' will create it if is not already present.
    # Note: You can also use "a" for append mode.
    with open(output, 'w+', encoding='utf-8', newline='') as csvfile:
        outputwriter = csv.writer(csvfile, dialect='excel')  # We will call outputwriter later...
        # This file has tens of lines. We should use a "for loop" to iterate
        # open() is a built-in library function to open a file. "r" means read mode
        for line in open(filepath, "r"):
            # re.compile() is a built-in library function to compile a regular expression
            # regex_email is the variable which saves the regular expression '[\w\.-]+@[\w\.-]+'
            regex_email = re.compile("[\w.-]+@[\w.-]+")
            # re.findall() is a built-in library function to search all matched-pattern
            # substrings from a string. '[\w\.-]+@[\w\.-]+' is a regular expression
            matches = re.findall(regex_email, line)
            # If the matched-pattern substrings are found, the variable of "matches" save them
            # We have to check if the variable is empty/null
            if not matches:
                # If the variable of "matches" is empty/null, ignore the following codes and continue
                # with the next loop
                continue
            for match in matches:
                print("The extracted email address is :" + match)
                outputwriter.writerow([match])

if __name__ == "__main__":
    main()
