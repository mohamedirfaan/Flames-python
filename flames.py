print('''
         |FFFFFFFFFFFF  ||                      A        M      M   EEEEEEEEE    SSSSSSSSSSS
         |              ||                     A A       M M   M M  EE           SS
         |              ||                    A   A      M  M M  M  EE           SS 
         |FFFFFFF       ||                   AAAAAAA     M   M   M  EEEEEEE      SSSSSSSSSSSSS  
         |              ||                  A       A    M       M  EE                      SS 
         |              ||============     A         A   M       M  EEEEEEEEE    SSSSSSSSSSSSS ''')
a=list(input("Enter your name : ").lower())
b=list(input("enter your crush name : ").lower())
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]==b[j]):
            a[i]='#'
            b[j]='#'
count=0
for i in a:
    if(i!='#'):
        count+=1
for i in b:
    if(i!='#'):
        count+=1
#print(count)
r=['F','L','A','M','E','S']
a=len(r)
key=1
index=0
count1=0
for i in range(1,10000):
    if key==count*5+1:
        break
    if index==a:
        index=0
    if(r[index]!='#'):
        if key%count==0 :
            r[index]='#'
        key+=1
    index+=1
for i in r:
    if i!='#':
        relate=i
print(relate,count)
relatedict={"F":"Friend","L":"Lover","A":"Affection","M":"Marriage","E":"Enemy","S":"Sibling"}
print("\n\nRelation ship status:",relatedict[relate],"\n\n")