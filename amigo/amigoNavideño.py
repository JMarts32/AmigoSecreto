from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt
import random

amigos = ["Martin Santos", "Nohora Ayala", "Juan Martin Santos", "Angelica Yepes", "Silvia Santos", "Tia Rochis",
          "Tia Alicia", "Ciro Ayala", "Cristina Mojica", "Jennifer Ayala", "David Ayala"]

amigoNavidenio = {"Martin Santos": "", "Nohora Ayala": "", "Juan Martin Santos": "", "Angelica Yepes": "",
                  "Silvia Santos": "", "Tia Rochis": "", "Tia Alicia": "", "Ciro Ayala": "", "Cristina Mojica": "",
                  "Jennifer Ayala": "", "David Ayala": ""}

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