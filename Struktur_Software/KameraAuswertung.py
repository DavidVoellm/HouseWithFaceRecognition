from Bibliotheken import *
import cv2

personen_handler = PersonenHandler()
camera = Camera()
erkennung = Gesichtserkennung()
personen_handler.find("./Daten")

erkennung.set_personen(personen_handler.get_personen())

frame = camera.get_frame()
cv2.imwrite("./frame.jpg", frame)
unknown_image = frame

berechtigtePersonenImBild = erkennung.get_face_names(unknown_image)
print(berechtigtePersonenImBild)