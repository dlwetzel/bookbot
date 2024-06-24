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
    
    count_words()
    
main()
