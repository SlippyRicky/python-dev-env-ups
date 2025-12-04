import numpy as np
from time import sleep

def cube(x):
    return x ** 3

def sphere_volume(r):
    return (4 * np.pi * r**3) / 3

def pyramide_et_cone_volume(b, h, is_cone=False):
    if is_cone:
        return (np.pi * b**2 * h) / 3
    else:
        return (b * h) / 3

def volume(L, forme, l=None):
    if forme == "cube":
        return cube(L)
    elif forme == "sphere":
        return sphere_volume(L)  # L est le rayon
    elif forme == "cone":
        if l is None:
            raise ValueError("Le cône nécessite un rayon et une hauteur.")
        return pyramide_et_cone_volume(L, l, is_cone=True)
    elif forme == "pyramide":
        if l is None:
            raise ValueError("La pyramide nécessite une largeur de base et une hauteur.")
        return pyramide_et_cone_volume(L, l)
    else:
        raise ValueError("Forme non reconnue.")

def afficher_ascii(forme):
    if forme == "cube":
        print("""
+------+.      +------+       +------+       +------+      .+------+
|`.    | `.    |\     |\      |      |      /|     /|    .' |    .'|
|  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |
|   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
+---+--+.  |   +-+----+ |     +------+     | +----+-+   |  .+--+---+
 `. |    `.|    \|     \|     |      |     |/     |/    |.'    | .'
   `+------+     +------+     +------+     +------+     +------+'
        """)
    elif forme == "sphere":
        print("""
              ::...:::!!!*o
         ..............::!!*oo
      ..................::!!**ooe
    .....................::!!**ooee
   .......................::!!**ooee
  ........................::!!**oooee
 .........................::!!**oooeee
:........................::!!!**oooeeee
........................::!!!**ooooeeee
:......................::!!!***oooeeeee
:....................:::!!!***oooeeeeee
!:.................:::!!!****oooeeeeeee
*!:::...........::::!!!!***ooooeeeeeeee
 *!!!:::::::::::!!!!!*****oooooeeeeeeeee
  o**!!!!!!!!!!!!!*****oooooeeeeeeeee
   oo**************ooooooeeeeeeeeeee
    eoooooooooooooooooeeeeeeeeeeeee
      eeeooooooooeeeeeeeeeeeeeeee
         eeeeeeeeeeeeeeeeeeeee
             eeeeeeeeeeeee
        """)
    elif forme == "cone":
        print("""
          ,`.
        ,'   `.
      ,'       `.
    ,'           `.
  ,'               `,
 '.                _-`
    '- ._  __ .- '
        """)
    elif forme == "pyramide":
        print("""
          ,/`.
        ,'/ __`.
      ,'_/_  _ _`.
    ,'__/_ ___ _  `.
  ,'_  /___ __ _ __ `.
 '-.._/___...-"-.-..__`.
        """)

def main():
    while True:
        print("\nChoisissez une forme parmi : cube, sphere, cone, pyramide (ou 'quitter' pour arrêter).")
        R = input("Voulez-vous calculer le volume d'un cube, d'une sphère, d'un cône, ou d'une pyramide ? ").lower()
        if R == 'quitter' or R == 'q':
            break
        if R not in ['cube', 'sphere', 'cone', 'pyramide']:
            print("Forme non reconnue.")
            sleep(1)
            print("Voulez vous voir un mechant soldat?")
            sleep(0.9)
            print(r"""

                           __.--|~|--.__                               ,,;/;
                         /~     | |    ;~\                          ,;;;/;;'
                        /|      | |    ;~\\                      ,;;;;/;;;'
                       |/|      \_/   ;;;|\                    ,;;;;/;;;;'
                       |/ \          ;;;/  )                 ,;;;;/;;;;;'
                   ___ | ______     ;_____ |___....__      ,;;;;/;;;;;'
             ___.-~ \\(| \  \.\ \__/ /./ /:|)~   ~   \   ,;;;;/;;;;;'
         /~~~    ~\    |  ~-.     |   .-~: |//  _.-~~--,;;;;/;;;;;'
        (.-~___     \.'|    | /-.__.-\|::::| //~     ,;;;;/;;;;;'
        /      ~~--._ \|   /          `\:: |/      ,;;;;/;;;;;'
     .-|             ~~|   | /V"" ""V\ |:  |     ,;;;;/;;;;;' \
    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;
   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\
  / \        \                             ,;;;;/;;;;;'     /    |
 |            |                          ,;;;;/;;;;;'      |     |
|`-._          |                       ,;;;;/;;;;;'              \
|             /                      ,;;;;/;;;;;'  \              \__________
(             )                 |  ,;;;;/;;;;;'      |        _.--~
 \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~
 \__         '  `  ._.        ,;;;;;/;;;;;'    .   /  \   / /~
 /          \'  |`._______ ,;;;;;;/;;;;;;'    /   :    \/'/'       /|_/|   ``|
| _.-~~~~-._ |   \ __   .,;;;;;;/;;;;;;' ~~~~'   .'    | |       /~ (/\/    ||
/~ _.-~~~-._\    /~/   ;;;;;;;/;;;;;;;'          |    | |       / ~/_-'|-   /|
(/~         \| /' |   ;;;;;;/;;;;;;;;            ;   | |       (.-~;  /-   / |
|            /___ `-,;;;;;/;;;;;;;;'            |   | |      ,/)  /  /-   /  |
 \            \  `-.`---/;;;;;;;;;' |          _'   | |    /'('  /  /|- _/  //
   \           /~~/ `-. |;;;;;''    ______.--~~ ~\  | |  ,~)')  /   | \~-==//
     \      /~(   `-\  `-.`-;   /|    ))   __-####\ | |   (,   /|    |  \
       \  /~.  `-.   `-.( `-.`~~ /##############'~~)| |   '   / |    |   ~\
        \(   \    `-._ /~)_/|  /############'       | |      /  \     \_\  `\
        ,~`\  `-._  / )#####|/############'   /     | |  _--~ _/ | .-~~____--'
       ,'\  `-._  ~)~~ `################'           | | ((~>/~   \ (((' -_
     ,'   `-.___)~~      `#############             | |           ~-_     ~\_
 _.,'        ,'           `###########              | |            _-~-__    (
|  `-.     ,'              `#########       \       | |          ((.-~~~-~_--~
`\    `-.;'                  `#####"                | |           "     ((.-~~
  `-._   )               \     |   |        .       |  \                 "
      `~~  _/                  |    \               |   `---------------------
        |/~                `.  |     \        .     |  O    __.---------------
         |                   \ ;      \             |   _.-~
         |                    |        |            |  /  |
          |                   |         |           |/'  |

             """)
            continue

        if R == "sphere":
            rayon = float(input("Quel est le **rayon** de la sphère ? "))
            vol = volume(rayon, R)
        elif R in ['cone', 'pyramide']:
            base = float(input("Quel est le rayon (cône) ou la largeur de la base (pyramide) ? "))
            hauteur = float(input("Quelle est la hauteur ? "))
            vol = volume(base, R, hauteur)
        else:  # cube
            largeur = float(input("Quel est la largeur du cube ? "))
            vol = volume(largeur, R)

        afficher_ascii(R)
        print(f"Le volume de la {R} est : {vol:.2f}")

if __name__ == "__main__":
    main()
