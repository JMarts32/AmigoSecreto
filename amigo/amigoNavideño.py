from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt
import random

amigos = ["Cecilia Santos","Paula Perucho","Abelino Perucho","Luisa Santos","Alba Lucia Santos",
          "Karol Fabiana","Lola Santos","Toya Santos","Alejandro Santos","Cecilia Neisa","Daniel Santos",
          "Maria Alejandra Santos","Martin Santos","Nohora Ayala","Silvia Santos","Juan Martin Santos",
          "Isabella Cadena","Nohema Santos","Pedro Castillo","Yolanda Santos","Savi","Hagee Olaya"]

amigoNavidenio = {"Cecilia Santos": "", "Paula Perucho": "", "Abelino Perucho": "", "Luisa Santos": "",
                  "Alba Lucia Santos": "", "Karol Fabiana": "", "Lola Santos": "", "Toya Santos": "",
                  "Alejandro Santos": "", "Cecilia Neisa": "", "Daniel Santos": "", "Maria Alejandra Santos": "",
                  "Martin Santos": "", "Nohora Ayala": "", "Silvia Santos": "", "Juan Martin Santos": "",
                  "Isabella Cadena": "", "Nohema Santos": "", "Pedro Castillo": "", "Yolanda Santos": "",
                  "Savi": "", "Hagee Olaya": ""}

contrasenias = []

for amigo in amigoNavidenio:
    number = random.randint(0, len(amigos) - 1)
    amigoNavidenio[amigo] = amigos[number]
    amigos.remove(amigos[number])

    formato = "El amigo secreto de " + amigo + " es " + amigoNavidenio[amigo]

    passwordString = amigo + str(number)    
    contrasenias.append(passwordString)
    password = pdfencrypt.StandardEncryption(passwordString)

    nombre = "Files/" + amigo + ".pdf"
    c = canvas.Canvas(nombre,bottomup=0,encrypt=password)
    c.drawString(100, 750, formato)
    c.save()


file = open("Files/contra.txt", "w")

for contrasenia in contrasenias:
    file.write(contrasenia + "\n")

file.close()

