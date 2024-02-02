cap_list=[]
cap_dict=dict()
word=''
i=0
new_index=0
paragraph=input('Enter your sentences:')
first_of_sentence=1
for i in range(0,len(paragraph)):
    if new_index!=0:
        i=new_index
        new_index+=1
    if first_of_sentence==1:
        i+=1
        new_index+=1
        first_of_sentence=0
    if (i>=len(paragraph)-1):
        break
    if paragraph[i]=='.':
        first_of_sentence=1
        i+=1
        new_index+=1
    if paragraph[i].isupper()==True:
        while paragraph[i]!=' ' :
            if paragraph[i]=='.':
                first_of_sentence=1
                i+=2
                new_index+=2
                break
            word=word+paragraph[i]
            i+=1
            new_index=i
        cap_list.append(word)
        word=''
for item in cap_list:
    cap_dict[item]=cap_dict.get(item,0)+1
for cap_word in list(cap_dict.keys()):
    print('%s:%s' %(cap_word,cap_dict[cap_word]))
