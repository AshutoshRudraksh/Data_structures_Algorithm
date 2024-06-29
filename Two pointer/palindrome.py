# palidrome 
def ispalindrome(word):
  L, R  = 0 , len(word) -1
  while L<R:
    if word[L] != word[R]:
      return False
    L+=1
    R-=1
  return True