# #!/usr/bin/python
# Python program to count the frequency of word in the sentence

if __name__ == '__main__':
    print "Enter the sentence :"
    sentence = raw_input()
    print "Enter a word :"
    word = raw_input()
    list1 = sentence.split(' ')

    count = 0
    for w in list1:
        if word == w:
            count = count + 1
    print "Count of word in the sentence is: %i"%count
