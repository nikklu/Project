#create a word with less thenn 12 words
#no spaces 
#no numbers
res=input("Enter a word:")
if len(res)<12:
    print("The word is less than 12 characters.")
elif not res.find(" ")==1:
    print("The word contains spaces.")
elif not res.isalpha():
    print("The word contains numbers.")