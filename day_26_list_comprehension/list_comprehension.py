new_list = [i*2 for i in range(1,5)]
print(new_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [i for i in names if len(i) < 5]
print(short_names)

long_names = [i.upper() for i in names if len(i) > 5]
print(long_names)