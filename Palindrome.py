# #!/usr/bin/python

# Python program to check if the word is a palindrome  or not

def palindrome(string1):
        list1=list(string1)
        len1=len(list1)
        i=0
        n=len1
        while i<= n:
          if list1[i] == list1[n-1]:
             flag=0
          else:
             flag=1
             break
          i=i+1
          n=n-1
        if flag == 0:
           print "The string is palindrome"
        else:
           print "The string is not palindrome"

if __name__ == '__main__':
        print "Enter a string:"
        str1 = raw_input()
        palindrome(str1)
