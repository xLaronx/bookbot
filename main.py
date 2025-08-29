from stats import word_count,dictionary,report

def get_book_text(path_to_file):
        with open(path_to_file) as f:
            return f.read()
def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)    
    chars_dict = dictionary(text)
    words = word_count(text)
    main_report= report(chars_dict)
    
    print("============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt... \n----------- Word Count ----------")
    print(f"Found {words} total words\n--------- Character Count -------")
    for entry in main_report:
        print(f"{entry['char']}: {entry['num']}")
    print(f"============= END ===============")
main()