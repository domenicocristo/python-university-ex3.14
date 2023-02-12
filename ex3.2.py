"""
1. Modificate do_twice in modo che accetti due argomenti, un oggetto funzione e un valore, 
e che chiami la funzione due volte passando il valore come argomento.

2. Copiate nel vostro script la definizione di print_twice che abbiamo visto nel corso di
questo capitolo.

3. Usate la versione modificata di do_twice per chiamare print_twice per due volte,
passando spam come argomento.
"""

def do_twice(func, arg):    
    func(arg)
    func(arg)

def print_twice(arg):    
    print(arg)
    print(arg)

do_twice(print, 'spam')
print('')

"""
4. Definire una nuova funzione di nome do_four che richieda un oggetto funzione e un
valore e chiami la funzione per quattro volte, passando il valore come argomento. Dovrebbero esserci 
solo due istruzioni nel corpo di questa funzione.
"""

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_four(print, 'spam')
