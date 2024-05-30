import sys
sys.stdin=open("in.txt","r")
sys.stdout=open("out.txt","w")
#declare
n=0
ins_name=[]
ins_ope=["IF ","RR ","ALU","DA ","RW "]
ins_opetime=[0,0,0,0,0]
INS_pineline=0;
#input
temp=input()
n=int(input())
temp=(input())
temp=input()
go=""
for i in range (len(temp)):
    if(temp[i]!='(' and temp[i]!=')'):
        go+=temp[i]
    elif (temp[i]==')'):
        ins_name.append(go)
        go=""
temp=input()
ins_opetime[0]=int(input())
temp=input()
ins_opetime[1]=int(input())
temp=input()
ins_opetime[2]=int(input())
temp=input()
ins_opetime[3]=int(input())
temp=input()
ins_opetime[4]=int(input())
nublock=5+n-1
INS_nopineline=0;
for i in range (5):
    INS_nopineline+=ins_opetime[i]
    INS_pineline=max(INS_pineline,ins_opetime[i])
print ("speed up ",INS_nopineline/INS_pineline," times")
#write it to file
fcol=""
bkspace=[]
for i in range (nublock):
    bkspace.append(0)
bkspace.append(0)
for i in range(n):
    if(len(fcol)< len(ins_name[i])):
        fcol+=(" " * (len(ins_name[i]) - len(fcol)+1));
print(fcol,end="")
for i in range(n):
    if(len(fcol)> len(ins_name[i])):
        ins_name[i]+=(" " * abs(len(ins_name[i]) - len(fcol)));
time=0;
for i in range (nublock):
    v=str(time)
    bkspace[i]=len(v)
    print(time,"   ",end="")
    time+=INS_pineline
print(time)
#print(bkspace)
for i in range (n):
    print(ins_name[i],end="")
    for j in range(i):
        s1=bkspace[j]*' '
        print(s1,"   ",end="")
    for j in range(5):
        s1 = bkspace[i+j] * ' '
        print(s1,ins_ope[j],end="");
    print()


