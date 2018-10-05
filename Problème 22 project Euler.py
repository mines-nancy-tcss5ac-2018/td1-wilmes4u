
#TD n22
"""def listing(C):
    L=[]
    nom=''
    k=1
    if len(C)==0:
        return []
    else:
        while k!=len(C):
            if C[k]!='"':
                nom+=str(C[k])
                k+=1
            else:
                k+=1
                L.append(nom)
                nom=''
        LT=[]
        for j in range((len(L))):
            if str(L[j])!=',':
                LT.append(L[j])
        LT.sort()
        return LT"""


def tri_text(tex):
    L=tex.split(",")
    L.sort()
    return L



def score_nom(nom):
    sco=0
    for k in range(1,len(nom)-1):
        sco=sco+ord(nom[k])-ord('A')+1
    return sco

assert score_nom('"COLIN"')==53


def score_tot(tex):
    tot=0
    for k in range(len(tex)):
        tot+=(k+1)*score_nom(tex[k])
    return tot


text = open("p022_names.txt", "r")

print(score_tot(tri_text(text.read())))

#Resultat = 871198282



        
