def main():
    words = input("Text: ").split()
    censored_words = []
    for word in words:
        new_word = []
        for i in range(len(word)):
            if i % 2 == 0:
                new_word.append(word[i])
            else:
                new_word.append('*')
        censored_words.append(''.join(new_word))
    print('_'.join(censored_words))
