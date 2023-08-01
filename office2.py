source=input("Enter a source word")
while True:
    match=input("Enter a word to check for anagram")
    print("anagram") if sorted(source)==sorted(match) else print("not an anagram")
    print('Enter 0 to exit, 1 to continue')
    ch=int(input("Enter your choice"))
    if ch==0:
        break
