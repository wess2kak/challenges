def repetitions(input):
 substring_end = 1
 while substring_end <= len(input) * 0.5:
  substring = input[0:substring_end]
  quotient = int(len(input) / len(substring))
  matches = 0
  for attempt in range(quotient):
   start = len(substring) * attempt
   segment = input[start:start+len(substring)]
   if segment == substring:
    matches += 1
  if matches > 1 and matches == quotient:
   return True
  substring_end += 1
 return False

if __name__ == '__main__':
 test_words = ['abcabcabc', 'aaaaaaa', 'asdfasdf', 'aa', 'aaa', 'qwertyuiopwertyuiop', '123a123a', 'asdf123asdf123']
 print('Are the following strings made up of repeating segments?')
 for word in test_words:
  print(repetitions(word),'\t',word)
