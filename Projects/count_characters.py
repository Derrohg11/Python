#Python script to count the number of each character in a text file

#Open the text file for reading
with open("text.txt", "r") as file:
    text = file.read()

#Create an empty dictionary to store the character counts
char_count = {}

#Iterate through each character in the text
for char in text:
    #If the character is already in the dictionary, increment its count
    if char in char_count:
        char_count[char] += 1
    #If the character is not in the dictionary, add it with a count of 1
    else:
        char_count[char] = 1

#Print the character counts
for char, count in char_count.items():
    print(f"'{char}': {count}")