poem = open("E:\\Projects\\python-basics-exercises\\13_read_write_files\\poem.txt","r")

word_bag = {}

for line in poem:
    words = line.split()
    for word in words:
        if word in word_bag:
            word_bag[word]+=1
        else:
            word_bag[word] = 1

poem.close()
words_count = list(word_bag.values())
max_occurence = max(words_count)

for word,count in word_bag.items():
    if count == max_occurence:
        print(f"{word} => {count}") 
