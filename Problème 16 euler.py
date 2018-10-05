#TD n 16

def sum(n,b):
    num=b**n
    chaine=str(num)
    sum2=0
    for k in range(len(chaine)):
        sum2+=int(chaine[k])
    return sum2


assert sum(15,2)==26

#print(sum(1000,2))

#Reponse : 1366