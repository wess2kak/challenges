def substring_repetitions(input_str):
    """
    roughly equivalent to the builtin find method used in the following way:
    return (str+str)[1:-1].find(str) != -1
    """
    substring_end = 1
    while substring_end <= len(input_str) * 0.5:
        substring = input_str[0:substring_end]
        matches = 0
        for attempt in range(int(len(input_str) / len(substring))):
            segment = input_str[len(substring) * attempt:(len(substring) * attempt) + len(substring)]
            matches += 1 if segment == substring else 0
        if matches > 1 and matches == int(len(input_str) / len(substring)):
            last_letter_checked = segment[-1]
        if matches > 1 and matches == int(len(input_str) / len(substring)) and last_letter_checked == input_str[-1]:
            return True
        substring_end += 1
    return False


if __name__ == '__main__':
    test_words = ['asdfasdfa', 'abcabcabc', 'aaaaaaa', 'asdfasdf', 'aa', 'aaa', 'qwertyuiopwertyuiop', '123a123a', 'asdf123asdf123', '123a345b']
    print('Are the following strings made up of repeating segments?')
    for word in test_words:
        print(substring_repetitions(word), '\t', word)
