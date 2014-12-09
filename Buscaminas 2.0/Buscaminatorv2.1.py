import random
import string
import sys
import winsound , sys
sys.setrecursionlimit(2500)
#SONIDO CUANDO PIERDES
sound = 'explosion.wav'
sound2= 'win.wav'
def ganaste(sound2):
    winsound.PlaySound(sound2 , winsound.SND_FILENAME)
def perdiste(sound):
    winsound.PlaySound(sound , winsound.SND_FILENAME)
d2={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y', 51: 'Z'}
d={'i': 8, 'D': 29, 'e': 4, 'v': 21, 'E': 30, 'n': 13, 'f': 5, 'R': 43, 'm': 12, 'a': 0, 'J': 35, 'p': 15, 'T': 45, 'N': 39, 'V': 47, 'z': 25, 'M': 38, 'I': 34, 'q': 16, 'y': 24, 'G': 32, 'w': 22, 's': 18, 'P': 41, 'g': 6, 'h': 7, 'X': 49, 'x': 23, 'o': 14, 'Z': 51, 'H': 33, 'l': 11, 'L': 37, 'b': 1, 'k': 10, 'A': 26, 'K': 36, 'd': 3, 'O': 40, 'Q': 42, 'C': 28, 'u': 20, 't': 19, 'c': 2, 'B': 27, 'W': 48, 'r': 17, 'S': 44, 'j': 9, 'U': 46, 'F': 31, 'Y': 50}
global mov
def matriz():
    global lismin
    global lissel
    global lisloca1
    global listan
    while True:
        lismin=[]
        lissel=[]
        listan=[]
        for x in range(0,tam):
            lismin.append("")
            lissel.append(False)
        for x in range(0,minas):
            lismin.remove("")
            lismin.append("*")
        random.shuffle(lismin)
        lissel=lol(lissel,lenght)
        lismin=lol(lismin,lenght)
        for x in range(0,lenght):
            for y in range(0,lenght):
                listan.append(vecinos(x,y,lismin))
        listan=lol(listan,lenght)
        for x in range(lenght):
            for y in range(lenght):
                if listan[x][y]=="*":
                    lisloca1.append((x,y))
        lisloca1.sort()
        return
def revelar():
    global lisloca
    global conta
    conta=0
    global mov
    while True:
        conta+=1
        c1=0
        c2=0
        flg=False
        y=""
        x=""
        if conta==1:
            inp=str(input("Ingrese la casilla a abrir (ej.a5,D32flag): "))
        if conta!=1:
            inp=str(input("Input incorrecto, vuelva a intentarlo: "))
        inp=inp.replace(" ","")
        if inp in["quit","QUIT","Quit","RESTART","restart","SALIR","salir","Salir","Reiniciar","REINICIAR","reiniciar"]:
            while True:
                input2=input("Seguro que desea abandonar la partida? (si/no): ")
                if input2 in ["SI","Si","si","S","s","sI","yes","y","Y","YES"]:
                    return False
                if input2 in ["NO","No","no","Nel","N","n","nO"]:
                    conta=0
                    break
        for i in ["flag","FLAG","Flag","flg","FLG"]:
            if i in inp:
                inp=inp.replace(i,"")
                flg=True
        inpb=""
        for i in range(len(inp)):
            if inp[i].isalnum():
                inpb=inpb+inp[i]
        inp=inpb
        inp2=inp
        for m in ["1","2","3","4","5","6","7","8","9"]:
            for n in range(len(inp2)):
                if  m==inp2[n]:
                    c1+=1
        for i in string.ascii_letters:
            for w in range(len(inp2)):
                if i == inp2[w]:
                    c2+=1 
        if c2!=1:
            if c1!=1 or c1!=2:
                continue
        for i in range(len(inp)):
            if inp[i].isdigit():
                x=str(x)+inp[i]
        inp=inp.replace(x,"")
        x=int(x)-1
        y=d[inp]
        inp=inp.replace(d2[y],"")
        if existe(x,y,listan)==False:
            continue
        if flg:
            if lissel[x][y]==True:
                continue
            if lissel[x][y]=="F":
                lisloca.remove((x,y))
                lisloca.sort()
                lissel[x][y]=False
                return True
            if not lissel[x][y]:
                lisloca.append((x,y))
                lisloca.sort()
                lissel[x][y]="F"
                return True
        if lissel[x][y]==False and inp==""  and x>-1 and x<52 and y<52 and y>-1 :
            break
    while mov==1 and listan[x][y]=="*":
        matriz()
        break
    if listan[x][y]=="*":
        #AGREGAR SONIDO DE EXPLOSION
        perdiste(sound)
        global lenght
        lisselab=[]
        for x in range(0,tam):
            lisselab.append(True)
        lisselab=lol(lisselab,lenght)
        imprimir(listan,lisselab,0,0)
        print("\nHas perdido... PERDEDOR")
        return False
    if listan[x][y]==0:
        ceros(x,y)
        return True       
    if not lissel[x][y]:
        lissel[x][y]=True
        return True
def ceros(x,y):
    lissel[x][y]=True
    for a in range(-1,2):
        for b in range(-1,2):
            if not( a ==0 and b==0):
                if existe(x+a,y+b,listan):
                    if not lissel[x+a][y+b]:
                        if listan[x+a][y+b]==0:
                            lissel[x+a][y+b]=True
                            ceros(x+a,y+b)
                        if listan[x+a][y+b] in(1,2,3,4,5,6,7):
                            lissel[x+a][y+b]=True
    return 
def imprimir(tablero,tabbol,mov,contacer):
    lenght=len(tablero)
    arriba="     "
    for x in range(0,lenght):
        arriba=arriba+d2[x] +"   "
    arriba="\n"+arriba
    linea="   "
    for x in range(0,lenght*4+1):
        linea=linea+"-"
    arriba=arriba+"\n"+linea+"\n"
    vimp=""
    for x in range(0,lenght):
        for y in range(0,lenght):
            if y ==0 and x<9:
                vimp= vimp+str(x+1)+"  |"
            if y ==0 and x>8:
                vimp= vimp+str(x+1)+" |"
            if tabbol[x][y]=="F":
                vimp=vimp+ "[F]|"
            if tabbol[x][y]==False:
                vimp=vimp+ "[ ]|"
            if tabbol[x][y]==True:
                vimp=vimp+ "["+(str(tablero[x][y]))+"]|"
        vimp=vimp+"\n"+linea+"\n"
    if mov>0:
        vimp= vimp+"\n\nTurno numero "+str(mov)+"\nCasillas cerradas (Incluye flags):"+str(contacer)+"\n"
    arriba=arriba+vimp             
    return print(arriba)
def vecinos(fila,columna,univ):
    if univ[fila][columna]=="*":
        return "*"
    cantvec=0
    for a in range(-1,2):
        for b in range(-1,2):
            px2=fila+a
            py2=columna+b
            if existe(px2,py2,univ):
                if univ[px2][py2]=="*":
                    cantvec+=1
    return cantvec
def nivel():
    global niv
    global tam
    global minas
    niv = 0
    global cdj
    global lenght
    tam=0
    while True:
        tam=input("\nIngrese el tamano del tablero (Minimo 9, maximo 52): ")
        if (tam.isnumeric()):
            tam= int(tam)
            if tam>8 and tam<53:
                break
    lenght=tam 
    while niv != "1"and niv != "2"and niv != "3"  and niv!="4" :
        niv = input("\nEscoge el nivel a jugar (1, 2, o 3): ")
        if niv in ["1","2","3","4"]:
            niv=int(niv)
        if niv == 1:
            minas=int(tam**1.25)
            print("\nNivel 1")
            print("\nMinas: "+str(minas))
            return print("")
        elif niv ==2:
            minas=int(tam**1.4)
            print("\nNivel 2")
            return print("")
        elif niv == 3:
            minas=int(tam**1.5)
            print("\nNivel 3")
            return print("")
        elif niv == 4:
            niv=4
            minas=int((tam**1.7)+1)
            print("\nNivel 4")
            return print("")
def existe(w,v,universo):
    lenght2=range(lenght)
    if 1==lenght2.count(w):
        if 1==lenght2.count(v):
            return True
    return False
lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
cdj=-1
while True:
    nivel()
    global lisloca
    global lisloca1
    lisloca=[]
    lisloca1=[]
    global mov
    mov=0
    cdj+=1
    if cdj==0:
        print("Escoja la casilla ingresando la cordenada (Ej.b6).Al seleccionar una coordenada con mina, perdera. Si cree que alguna cordenada contiene una mina: Escriba la coordenada junto con la palabra flag; esto bloqueara la celda y no se podra abrir. Para ganar: abra todas las casillas que no contienen una mina o flageelas. Si desea reiniciar el juego solo introduzca \"quit\".")
    global listan
    global lissel
    global tam
    global contacer
    tam=tam**2
    global lenght
    matriz()
    imprimir(listan,lissel,mov,0)
    while True:
        mov+=1
        if not revelar():
            break
        contacer=0
        cntdr=0
        for x in range(0,lenght):
            for y in range(0,lenght):
                if False== lissel[x][y] or lissel[x][y]=="F":
                    contacer+=1
                if False==lissel[x][y]:
                    cntdr+=1
        if contacer==minas or lisloca==lisloca1:
            ganaste(sound2)
            print("Felicidades has ganado... CAMPEON!!!\n")
            lisselab=[]
            for x in range(0,tam):
                lisselab.append(True)
            lisselab=lol(lisselab,lenght)
            imprimir(listan,lisselab,0,0)        
            break
        imprimir(listan,lissel,mov,cntdr)
    seguir=""
    while (seguir!="Si" and seguir!="nO" and seguir !="NO"and seguir!= "YES"and seguir !="No" and seguir !="yes" and seguir !="no" and seguir !="SI"and seguir !="si"and seguir!="s"):
        seguir=str(input("\nVolver a jugar? (Si/No) : "))
        seguir=seguir.replace(" ","") 
    if (seguir=="No" or seguir=="no"or seguir=="NO" or seguir=="nO"):
        break
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Graciaspor jugar.\nHecho por:\n\n")
print("  ___ ___ .__     __             ___________________           .__                ")
print(" /   |   \|__|   |__| ____  _____\______ \__    ___/_ _________|__| ____    ____  ")
print("/    ~    \  |   |  |/  _ \/  ___/|    |  \|    | |  |  \_  __ \  |/    \  / ___\ ")
print("\    Y    /  |   |  (  <_> )___ \ |    `   \    | |  |  /|  | \/  |   |  \/ /_/  >")
print(" \___|_  /|__/\__|  |\____/____  >_______  /____| |____/ |__|  |__|___|  /\___  / ")
print("       \/    \______|          \/        \/                            \//_____/  ")
print("...porfavor ponganos 10, POR FAVOR!!!!")
print("el primer hijo de josue se llamara Ramon si nos pone 10!!!")
import os
os._exit(0)


