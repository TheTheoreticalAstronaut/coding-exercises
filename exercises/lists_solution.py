def sort_strings_lowercase(list):
    return sorted([str.lower() for str in list])

def sum_string_characters(str):
    return [c for c in str.lower() if c.isalpha()]