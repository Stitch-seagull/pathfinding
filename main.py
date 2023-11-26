import Labyrinthe
import tkdraw.basic as graph

laby = Labyrinthe.creer(15,15)
for ligne in laby:
    print(ligne)

"""
Exemple :

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
[0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
[0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1]
[0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
[0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
[0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
[0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 3, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

0 = Mur ⬛
1 = Passage ⬜
2 = Point de départ 🟦
3 = Point d'arrivée 🟪
4 = Chemin déjà emprunté par algorythme de résolution 🟫
5 = Chemin solution 
"""

hauteur = 300
largeur = 300
graph.open_win(hauteur,largeur)

"""
0 -----> X
|
|
↓ 
Y

"""

def rectangle(x1, x2, y1, y2, color):
    for y in range(x1,x2):
        for x in range(y1, y2):
            graph.plot(x,y,color)

def StartEndPointFinder(gridToLook):
    result = [None, None]

    for j in range(len(gridToLook)):
        for i in range(len(gridToLook[0])):
            if(gridToLook[j][i] == 2 or gridToLook[j][i] == 3):
                result[gridToLook[j][i] - 2] = (j, i)
    return result

def pathFinder(gridToSolve, sP, eP, historic):
    gdhb = [(sP[0], sP[1] - 1),(sP[0], sP[1] + 1),(sP[0] + 1, sP[1]),(sP[0] - 1, sP[1])]
    # Coordonnées tel que [gauche, droite, haut, bas]
    for coordinates in gdhb: 
        match gridToSolve[coordinates[0]][coordinates[1]]:
            case 1:
                gridToSolve[coordinates[0]][coordinates[1]] = "4"
                pathFinder(gridToSolve, coordinates, eP, (historic + [coordinates]))

            case 3 :
                print("Arrivé !")
                print("Historique :" + str(historic))
                for pathCaseCoordinates in historic:
                    gridToSolve[pathCaseCoordinates[0]][pathCaseCoordinates[1]] = 5

        
def labyRender(larg, haut, labyGrid):
    squareHaut = haut // len(labyGrid)
    squareLarg = larg // len(labyGrid[0])
    colorDictionnary = {"0" : "#000000", "1" : "#ffffff", "2" : "#377d78", "3" :"#613140", "4" : "#f0ce9e", "5" : "#888eb5"}

    # Chaque ligne
    for j in range(len(labyGrid)):
        #Chaque colonne
        for i in range(len(labyGrid[0])):
            rectangle(i * squareLarg, (i+1) * squareLarg, j * squareHaut, (j + 1) * squareHaut, colorDictionnary[str(labyGrid[j][i])])
            graph.refresh()


pathFinder(laby, StartEndPointFinder(laby)[0], StartEndPointFinder(laby)[1], [])
labyRender(largeur, hauteur, laby)
graph.wait()