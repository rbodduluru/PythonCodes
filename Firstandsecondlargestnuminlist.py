# #!/usr/bin/python

# Python program to find the largest and second largest numbers from the list

def firseclargest(list1):
    
    unique_numbers = set(list1)

    largest_number = max(unique_numbers)

    print "Largest number in the list is :%i"%largest_number

    unique_numbers.remove(largest_number)

    second_largest_number = max(unique_numbers)

    print "Second largest number in the list is :%i"%second_largest_number


if __name__ == '__main__':

    list1 = []
    maxNumbers = 5

    while len(list1) < maxNumbers:
        numbers = input("Enter the numbers :")
        list1.append(numbers)

    firseclargest(list1)
