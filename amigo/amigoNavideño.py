from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt
import random

amigos = [
    "Tia Ceci",
    "Tia Luisa",
    "Ceci Neisa",
    "Tia Yaya",
    "Tia Alba",
    "Tio Alejandro",
    "Tia Toya",
    "Tia Lola",
    "Avelino",
    "Hagee",
    "Paula",
    "Carlos",
    "Savi",
    "Isa",
    "Diego",
    "Maja",
    "Fabiana",
    "Tia Nohe",
    "Don Pedro",
    "Jorge"
]

amigoNavidenio = {"Tia Ceci": "", "Tia Luisa": "", "Ceci Neisa": "",
                  "Tia Yaya": "", "Tia Alba": "", "Tio Alejandro": "",
                  "Tia Toya": "", "Tia Lola": "", "Avelino": "", "Hagee": "",
                  "Paula": "", "Carlos": "", "Savi": "", "Isa": "", "Diego": "",
                  "Maja": "", "Fabiana": "", "Tia Nohe": "", "Don Pedro": "", "Jorge": ""}

contrasenias = []

for amigo in amigoNavidenio:
    number = random.randint(0, len(amigos) - 1)
    while amigo == amigos[number]:
        number = random.randint(0, len(amigos) - 1)
    amigoNavidenio[amigo] = amigos[number]
    amigos.remove(amigos[number])

    formato = "El amigo secreto de " + amigo + " es " + amigoNavidenio[amigo]

    passwordString = amigo + str(number)    
    contrasenias.append(passwordString)
    password = pdfencrypt.StandardEncryption(passwordString)

    nombre =  amigo + ".pdf"
    c = canvas.Canvas(nombre,bottomup=0,encrypt=password)
    c.drawString(100, 750, formato)
    c.save()


file = open("contra.txt", "w")

for contrasenia in contrasenias:
    file.write(contrasenia + "\n")

file.close()

def calculate_number():
    number = random.randint(0, len(amigos) - 1)