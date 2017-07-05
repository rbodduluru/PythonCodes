# #!/usr/bin/python

# Python program to find the duplicate numbers in the list of numbers
def finddup(myList):
    for i in set(myList):
        if myList.count(i) > 1:
            print "Duplicate number(s) in the list : %i"%i

    
if __name__ == '__main__':
    myList = []
    maxNumbers = 10

    while len(myList) < maxNumbers:
        numbers = input("Enter numbers to find duplicates :")
        myList.append(numbers)
    finddup(myList)
