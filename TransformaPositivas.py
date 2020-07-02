import cv2
import os
from imutils import paths
import shutil

def listPosImagem():
    imagemPath = list(paths.list_images('imagens/comMascara'))
    cont = 1

    if not os.path.exists('pos'):
        os.makedirs('pos')

    for i in imagemPath:
        shutil.copy(i, i.replace(i, "pos/"+str(cont)+".png"))
        img = cv2.imread("pos/" + str(cont) + ".png", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img,(100,100))
        cv2.imwrite("pos/" + str(cont) + ".png", resized_image)

        cont+=1

listPosImagem()