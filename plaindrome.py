
#  this function returns true if word is a plaindrome else false
def plaindrome(word):

    return True if word[::-1] == word else False

print(plaindrome('lawal'))