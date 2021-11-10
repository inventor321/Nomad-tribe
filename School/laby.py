import random

def iota(n):
    return list(range(n))

def contient(tab, x):
    if x in tab:
        return True
    return False
    
def ajouter(tab, x):
    if not contient(tab, x):
        tab.append(x)
    return tab

def retirer(tab, x):
    if contient(tab, x):
        tab.remove(x)
    return tab

def voisins(x, y, nX, nY):
    case = y*nX + x
    cases = [] 
    if y != 0:
        cases.append(case-nX)
    if x != 0:
        cases.append(case-1)
    if x+1 != nX:
        cases.append(case+1)
    if y+1 != nY:
        cases.append(case+nX) 
    return cases
    

def laby(nX, nY, largeurCase):
    cols = (nY*largeurCase)+1
    rang = (nX*largeurCase)+1
    
    mursV=iota((nX+1)*nY)
    mursH=iota((nY+1)*nX-1)
    mursH=retirer(mursH,0)
    
    cave=[int(random.random()*nX*nY)]
    for i in range(len(cave)):
        cave[i]
    grid = iota(nX*nY)
    
    grid = retirer(grid, cave[0])
    
    for k in range(nY*nX-1):
        celV=[]
        cel=[]
        for i in range(len(cave)):
            cel = voisins(cave[i]%nX,cave[i]//nX,nX,nY)
            for j in range(len(cel)):
                celV=ajouter(celV, cel[j])
        for i in range(len(cave)):
            celV=retirer(celV,cave[i])
        index = int(random.random()*len(celV))
        cel = voisins(celV[index]%nX,celV[index]//nX,nX,nY)
        for i in range(len(grid)):
            cel = retirer(cel, grid[i])
        celluleChoisit = cel[int(random.random()*len(cel))]
        cave=ajouter(cave,celV[index])
        grid=retirer(grid,celV[index])
        
        distanceEntreLesCellules = celV[index] - celluleChoisit
        if distanceEntreLesCellules == -nX:
            mursH = retirer(mursH,celluleChoisit%nX + celluleChoisit//nX * nX)
        elif distanceEntreLesCellules == nX:
            mursH = retirer(mursH,celluleChoisit%nX + (celluleChoisit//nX+1) * nX)
        elif distanceEntreLesCellules == -1:
            mursV = retirer(mursV,celluleChoisit%nX + celluleChoisit//nX * (nX+1))
        else:
            mursV = retirer(mursV,1 + celluleChoisit%nX + celluleChoisit//nX * (nX+1))
            
    setScreenMode(rang, cols)
    
    
    for i in range(rang):
        for j in range(cols):
            setPixel(i, j, struct(r=15, b=15, g=15))
            
    for i in range(len(mursH)):
        for j in range(largeurCase+1):
            setPixel(mursH[i]%nX*largeurCase+j, mursH[i]//nX*largeurCase, struct(r=0, b=0, g=0))
            
    for i in range(len(mursV)):
        for j in range(largeurCase):
            setPixel(mursV[i]%(nX+1)*largeurCase, mursV[i]//(nX+1)*largeurCase+j, struct(r=0, b=0, g=0))
        
        
laby(4,4,20)