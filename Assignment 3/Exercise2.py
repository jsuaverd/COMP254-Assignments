
def palindrome(word):

    if len(word) <= 1:
        print("This is a palindrome")

    elif word[0] == word[-1]:
        palindrome(word[1:-1]) 
    else:
        print("not palindrome")


while True:
    word = input("Please enter a word (or 'exit' to quit): ")
    if word.lower() == 'exit':  
        break
    palindrome(word)


