import builtins

my_dictionary = {"key1": 1, "key2": 2}

k_list = ["key2", "key3", "key4", "key5"]

for i in k_list:

    if i in my_dictionary.keys():
        my_dictionary[i] = my_dictionary[i] + 1

    else:
        my_dictionary[i] = 0


