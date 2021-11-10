import turtle





nx = int(input("Largeur du labyrinthe"))
ny = int(input("Hauteur du labyrinthe"))
largeurCase = int(input("Largeur d'une case"))

turtle.hideturtle()
turtle.speed(9999999)

def carre(largeur):
    for _ in range(4):
        turtle.fd(largeur); turtle.lt(90)
def positionner(x, y):
    turtle.pu(); turtle.fd(x); turtle.lt(90); turtle.fd(y); turtle.rt(90); turtle.pd()
def grille(nx, ny, pas, largeur):
    for x in range(nx):
        for y in range(ny):
            positionner(x*pas, y*pas)
            carre(largeur)
            positionner(-x*pas, -y*pas)
positionner(-80, -50)
grille(nx, ny, largeurCase, largeurCase) # dessiner la grille
turtle.exitonclick()
print("done")