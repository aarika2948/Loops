word=input("Enter the word=").lower()
char=input("Enter the character=").lower()
if len(char)!=1:
    print("Invcalid Input")
i=0
count=0
while i<len(word):
    if word[i]==char:
        count+=1
    i+=1
print(f"The letter {char} has occured in {word} {count} times.")