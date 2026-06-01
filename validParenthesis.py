def validParenthesie(s):
  stack=[]
  mappin={'}':'{',']':'[',')':'('}
  opening={'{','[','('}
  for i in s:
    if i in opening:
      stack.append(i)
    elif stack and stack[-1]==mappin[i]:
      stack.pop()
    else:
       return False
    
  if stack:
    return False
  else:
    return True
#Example usage:
s = "((()))"        
result = validParenthesie(s)
print(result)  # Output: True
