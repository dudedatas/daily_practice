
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

my_dict2 = {}

for key,value in my_dict.items():
    my_dict2[value] = key


print(my_dict)
print(my_dict2)

