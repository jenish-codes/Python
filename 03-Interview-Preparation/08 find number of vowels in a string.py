

sentence = input('Enter a Sentence: ')
string = sentence.lower()
count = 0
list1 = ['a','e','i','o','u']
for i in string:
    if i in list1:
        count += 1
print('Number vowels is: ', count)
