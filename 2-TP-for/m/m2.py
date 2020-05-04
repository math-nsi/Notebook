# Fonction qui affiche la réponse
def affrep(vbool):
    if vbool:
        print('\x1b[5;32;48m' + 'Correct !' + '\x1b[0m')
    else:
        print('\x1b[5;31;48m' + 'Incorrect !' + '\x1b[0m')
        
# Fonction qui valide le TP01-for
def c1(f):
    if f()==483.93:
        test=True
    else:
        test=False
    affrep(test)
    
# Fonction qui valide le TP02-for
def c2(f):
    if f()==1230:
        test=True
    else:
        test=False
    affrep(test)
    
        
# Fonction qui valide le TP03-for
def c3(f):
    liste=[13*i for i in range(0,15)]
    if f()==liste:
        test=True
    else:
        test=False
    affrep(test)
    
# Fonction qui valide le TP04-for
def c4(f):
    liste=[3**i for i in range(0,10)]
    if f()==liste:
        test=True
    else:
        test=False
    affrep(test)
    
# Fonction qui valide le TP05-for
def c5(f):
    if f()==26917.37:
        test=True
    else:
        test=False
    affrep(test)
    
# Fonction qui valide le TP06-for
def c6(f):
    if f()==28656.28:
        test=True
    else:
        test=False
    affrep(test)  