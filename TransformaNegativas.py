import cv2
import os
from imutils import paths
import shutil

def listNegImagem():
    imagemPath = list(paths.list_images('imagens/semMascara'))
    cont = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in imagemPath:
        shutil.copy(i, i.replace(i, "neg/"+str(cont)+".png"))
        img = cv2.imread("neg/" + str(cont) + ".png", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img,(100,100))
        cv2.imwrite("neg/" + str(cont) + ".png", resized_image)

        cont+=1

listNegImagem()