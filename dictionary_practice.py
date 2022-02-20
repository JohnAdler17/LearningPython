def main():
    file = open('Lincoln.txt', 'r')
    my_dict = {}
    for line in file:
        line = line.rstrip()
        line = line.lower()
        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace('--', '')
        words = line.rsplit()
        for word in words:
            if word in my_dict:
                my_dict[word] += 1
            else:
                my_dict[word] = 1
    for word, occurances in my_dict.items():
        print('%s showed up %d time(s)' % (word, occurances))
    largest = 0
    max_word = ''
    for word, occurances in my_dict.items():
        currocc = occurances
        if largest < currocc:
            largest = currocc
            max_word = word
    print("The word", max_word, "appears", largest, "times.")
    file.close()
        

main()
