#TD n55

# Verifion en premier si le nombre est un palindrome
def palindrome(x):
    chiffre=str(x)
    k=0
    while k!=(len(chiffre))//2:
        if chiffre[k]==chiffre[-k-1]:
            k+=1
        else:
            return False
    return True

assert palindrome(121)==True


#Realisation du reverse

def reverse(x):
    chiffre=str(x)
    rev=''
    for k in range(len(chiffre)):
        rev+=chiffre[-k-1]
    return int(rev)

assert reverse(132)==231

def nb_Lychrel(n):
    nb=0
    i=1
    k=1
    while k<n:
        t=k
        while i<=50:
            if not palindrome(t+reverse(t)):
                t=t+reverse(t)
                i+=1
            else:
                k+=1
                t=k
                i=1
        nb+=1
        k+=1
        i=1
    return nb

#print(nb_Lychrel(10000))

#Reponse : 249
            
                    
                    
                    
            
        
            

