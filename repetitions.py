from datetime import datetime
def substring_repetitions(str):
    return (str+str)[1:-1].find(str) != -1

if __name__ == '__main__':
    test_words = ['aba', 'asdfasdfa', 'abcabcabc', 'aaaaaaa', 'asdfasdf', 'aa', 'aaa', 'qwertyuiopwertyuiop', '123a123a', 'asdf123asdf123', '123a345b', 'jwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamh',
                  'jwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamhjwAziCgMNxMfaoxSwamh']
    print('Are the following strings made up of repeating segments?')
    for word in test_words:
        start = datetime.now().timestamp()
        print(substring_repetitions(word), '\t', word)
        print((datetime.now().timestamp() - start) * 1000,'ms')
