# #!/usr/bin/python

# Python program to find if word is an anagram

if __name__ == '__main__':
    print "Enter word 1:"
    w1 = raw_input()
    print "Enter word 2:"
    w2 = raw_input()

    l1 = list(w1)
    l2 = list(w2)

    l1.sort()
    l2.sort()

    if l1 == l2:
        print "Its an anagram"
    else:
        print "Not an anagram"
