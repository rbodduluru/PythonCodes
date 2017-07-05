# #!/usr/bin/python

#Python program to find sum of numbers divisible by 3 and 5 in a given range

def sumofnum(n):

    return sum(p for p in xrange(n+1) if (p%3==0 or p%5==0 or (p%3==0 and p%5==0)))  

if __name__ == '__main__':

    print "Enter the range :"
    n = input()
    print "Sum of numbers divisible by 3 and 5 in Range is :%i"%sumofnum(n)
