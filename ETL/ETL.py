Read = input("Enter the name of txt file For Read :- ")

Write = input("Enter the name of txt file For Write :- ")

D = {}

#First Part:
#Extract (Reader)

with open(Read,'r') as F:

#Transformation


    fac = F.readlines()
    up = [x.upper() for x in fac]

#Load (Writer)
    
with open(Write,'w') as W:

    for i in up:
        W.write(i)

print ("The data is written in the",Write)

Write2 =  input("Enter the name of txt file For Write of second part :- ") 
#Second Part:
#Extract (Reader)

with open(Write,'r') as F:

#Transformation

    for line in F:
        words = line.split()
        for word in words:
            if word in D:
                D[word] = D[word] + 1
            else:
                D[word] = 1
            
#Load (Writer)
with open(Write2,'w') as W:
    for i in (D.keys()):
        W.write(i)
        W.write(' = ')     
        W.write(str(D[i]))
        W.write('\n')
print ("The data is written in the",Write2)
    
