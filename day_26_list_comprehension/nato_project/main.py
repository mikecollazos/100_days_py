import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key,value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #print(row)
#     #Access row.student or row.score
#     print(row.student)
#     if row.student == "Lily":
#         print(row.student)



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics_dict = {row.letter:row.code for (index,row) in df.iterrows()}
# print(df_dict)

#{"A": "Alfa", "B": "Bravo"}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = (input("Enter a word: ")).upper()
nato_list = [phonetics_dict[i] for i in name]

#nato_list = [value for key,value in df_dict.items() if key in new_list]


print(nato_list)


