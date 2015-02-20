__author__ = 'Applegrain'
#Lovisa Svallingson
#February 20th
#Create a program that checks if the word (input) is a palindrome

word = raw_input("Type the word you would like to check:")
print (word)

#List all the letters, have the indices be represented by letters
word_right = list(word)

#List all the letters in reverse order
reverse = word_right[::-1]

#See if the word is the same regardless of if you go from left->right, right->left
if word_right == reverse:
    print "Yes this word is a palindrome."
else:
    print "No, this word is not a palindrome."

