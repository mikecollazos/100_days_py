import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# try: 
#     file = open("a_file.txt", 'r')

# except Exception as e:
#     file = open("a_file.txt", 'w')
#     file.write("something")
#     print(f"{e} \n As a result, the file was now created")
    
# else:
#     print(file.read())

# finally:
#     raise TypeError("This is an error that i made up.")
#     # file.close()
#     # print("file was closed.")


height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height**2
print(bmi)

