import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



starting_letter = "Input/Letters/starting_letter.txt"
invited_names = "Input/Names/invited_names.txt"
output_path = "Output/ReadyToSend/"


with open(invited_names) as file:
    name_list = file.read().splitlines()

with open(starting_letter) as file:
    starting_content = file.read()

for name in name_list:
    new_content = starting_content.replace("[name]", name)
    
    with open(f"{output_path}letter_for_{name}.txt", "w") as file:
        file.write(new_content)


