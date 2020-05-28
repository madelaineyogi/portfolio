#pogoda

import random

print('Pozwól mi zgadnąć jaka jest u Ciebie pogoda!')

print('Jest...')

pogoda = random.randint(1, 3)

if pogoda == 1:
    print(' słonecznie?')
elif pogoda == 2:
    print(' śnieżyca?')
elif pogoda == 3:
    print(' deszczowo?')
else:
    print('Ciężo mi powiedzieć, chyba zasłoniłeś wszystkie okna!')
    
    
input('\n\nAby zakończyć program, naciśnij Enter')
