def commonPrefix(strs):
    if not strs:
         return ""
    strs.sort()
    first=strs[0]
    second=strs[-1]
    result=""
    for i in range(min(len(first),len(second))):
         if(first[i]!=second[i]):
              return result
         result+=first[i]
    return result
#Example usage:
strs = ["flower","flow","flight"]       
result = commonPrefix(strs)
print(result)  # Output: "fl"