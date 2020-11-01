def firstAlphabet(S):
    # code here
    l1=S.split()
    letters=''
    for word in l1:
        letters+=word[0]
    print(letters)

firstAlphabet('ssss bbb cccc')