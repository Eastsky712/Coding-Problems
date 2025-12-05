def count_word(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry file {filename} does not exist")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")
    
filenames = ['coding_practice/exceptions/alice.txt','coding_practice/exceptions/frankenstein.txt','coding_practice/exceptions/fairy_tale.txt','coding_practice/exceptions/moby_dick.txt']
for filename in filenames:
    count_word(filename)

