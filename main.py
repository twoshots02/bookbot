def open_book(book_path):
    with open(book_path) as f:
        
        file_contents = f.read()
        return file_contents

def word_count(str_to_count):
    chr_count = 0
    str_list = []

    str_list = str_to_count.split()
    chr_count = len(str_list)

    return chr_count

def count_characters(str_to_count):
    str_dict = {}
    string_to_process = ""
    string = ""
    string_to_process = str_to_count.lower()
    
    for string in string_to_process :
        if string.isalpha():
            if string in str_dict:
                str_dict[string] += 1
            else:
                str_dict[string] = 1
    return str_dict

def sort_dict(dict_to_sort):
    sorted_dict = sorted(dict_to_sort.items(), key=lambda item: (-item[1], item[0]))
    return sorted_dict

def report(file_name, file_text, character_count):
        reports = ""
        for char, count in character_count:
            reports += f"the '{char}' character was found {count} times\n"
        reports += "\n--- End report ---"
        print(f"--- Begin report of {file_name} ---")
        print(f"{word_count(file_text)} words found in the document.")
        print("\n")
               
        print(reports)
     
   

def main():
    file_text = ""
    test_string = "zxxaaaaabbbbbbbcccddeeeeeeeeee"
    file_name = "./books/frankenstein.txt"
    character_count_dict = {}
    character_count = []

    file_text = open_book(file_name)
    character_count_dict = count_characters(file_text)
    #character_count_dict = count_characters(test_string)
    character_count = sort_dict(character_count_dict)

    report(file_name, file_text, character_count)




main()