def clean_dict_empty_values(d):
    return {k: v for k, v in d.items() if v}

example_dict =  {"a": 24, "b": 42, "John": 58 , "c" : None}
example_dict["d"] = None
print(example_dict)
#{'a': 24, 'b': 42, 'John': 58, 'c': None, 'd': None}

cleaned_dict = clean_dict_empty_values(example_dict)
print(cleaned_dict)
# {'a': 24, 'b': 42, 'John': 58}
