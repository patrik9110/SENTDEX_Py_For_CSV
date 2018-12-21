import numpy as np

def main():
    date, rate, arb = np.loadtxt("TEST.csv", delimiter = ",", unpack = "True", dtype = "str")

    x = 0 #This will be equal to the rows on the for loop
    for eachDate in date[:-1]:
        saveLine = eachDate + "," + rate[x] + "," + arb[x] + "," + str(int(arb[x])+3) + "\n"
        saveFile = open("newTEST.csv", "a")
        saveFile.write(saveLine)
        saveFile.close()
        x += 1

    saveLine = date[-1] + "," + rate[x] + "," + arb[x] + "," + str(int(arb[x])+3)
    saveFile = open("newTEST.csv", "a")
    saveFile.write(saveLine)
    saveFile.close()

    saveLine = date[-1] + "," + rate[x] + "," + arb[x] + "," + str(int(arb[x])+3) + plusVar
    saveFile = open("newTEST.csv", "a")
    saveFile.write(saveLine)
    saveFile.close()

main()


    '''IGNORE:
    #CREAR UNA NUEVA COLUMNA QUE CONTIENE LA SUMA DE LA C5+C4 (C=columna, N=fila)
    x = 1 #se empieza en la segunda fila
    for eachDate in date[x:-1]:
        plusVar = str((int(arb[x-1])) + (int(arb[x]))) #suma la anterior fila de la misma columna mas la actual fila de la misma columna
        saveLine = eachDate + "," + rate[x] + "," + arb[x] + "," + str(int(arb[x])+3) + "," + plusVar + "\n"
        saveFile = open("newTEST.csv", "a")
        saveFile.write(saveLine)
        saveFile.close()
        x += 1 '''
