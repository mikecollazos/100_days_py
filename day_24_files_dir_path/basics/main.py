import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


with open("my_file.txt") as f:
    contents = f.read()
    print(contents)

with open("new_file.txt", "a") as f:
     f.write("\nnew text")