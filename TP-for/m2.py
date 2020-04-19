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