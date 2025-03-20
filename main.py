from stats import count_words, count_characters, sort_characters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
    return book_content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]  # ✅ Ensure the correct file is being passed

    text = get_book_text(file_path)  # ✅ Use file_path, not a hardcoded value
    num_words = count_words(text)
    char_count = count_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")  # ✅ Confirm correct file
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        print(f"{char}: {count}")

    print("============= END ===============")
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        

    file_path = sys.argv[1]


    text = get_book_text(file_path)
    num_words = count_words(text)
    chart_count = count_characters(text)
    print("============ BOOKBOT ============")


    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    sorted_chars = sorted(chart_count.items(), key=lambda item: item[1], reverse=True)
    for chart, count in sorted_chars:
        print(f"{chart}: {count}")


    print("============= END ===============")



if __name__ == "__main__":
    main()

