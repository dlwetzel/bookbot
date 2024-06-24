def main():
    
    frankenstein_path = "books/frankenstein.txt"

    
    def read_file():
        with open(frankenstein_path) as f:
            file_contents = f.read()
        return file_contents
    
    def count_words():
        file_contents_str = read_file()
        words = file_contents_str.split()
        print(len(words))
        
    def count_characters():
        chars = {}
        file_contents_str = read_file()
        for char in file_contents_str:
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        print(chars)
    
    count_characters()
    
main()
