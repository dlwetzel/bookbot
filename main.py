def main():
    
    frankenstein_path = "books/frankenstein.txt"

    
    def read_file():
        with open(frankenstein_path) as f:
            file_contents = f.read()
        return file_contents
    
    def count_words():
        file_contents_str = read_file()
        words = file_contents_str.split()
        return len(words)
    
    def sort_on(d):
        return d["num"]
        
    def count_characters():
        chars = {}
        chars_list = []
        file_contents_str = read_file()
        for char in file_contents_str:
            char = char.lower()
            if char in chars and char.isalpha():
                chars[char] += 1
            elif char.isalpha():
                chars[char] = 1
        for char in chars:
            chars_list.append({"char": char, "num": chars[char]})
        chars_list.sort(reverse=True, key=sort_on)
        return chars_list
        

    def print_report():
        num_words = count_words()
        chars_dict_list = count_characters()
        
        
        print(f"--- Begin report of {frankenstein_path} ---")
        for item in chars_dict_list:
            print(f"The '{item["char"]}' character was found {item['num']} times")
        print("--- End report ---")
            
        
        
    
    print_report()
    
main()
