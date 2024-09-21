def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letters(text)
    sorted_count = sort_letters(text)
    report = report_gen(sorted_count)
    print(f"{num_words} words found in the document")
    print()
    print("\n".join(report))
    print("--- End Report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letters(text):
    counts = {}
    lower = text.lower()
    for l in lower:
        if l.isalpha():
            if l in counts:
                counts[l] += 1
            else:
                counts[l] = 1
    return counts

def sort_on(item):
    return item[1]

def sort_letters(text):
    counts = get_letters(text)
    sorted_counts = []
    for letter, count in counts.items():
        sorted_counts.append((letter, count))
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts

def report_gen(sorted_count):
    report = []
    for letter, count in sorted_count:
        report.append(f"The '{letter}' character was found {count} times")
    return report
        


main()