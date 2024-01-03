#que muestre 15 numeros aleatorios

from guizero import App, Text, TextBox, PushButton
from random import randint

conca=""
ran=0
def imprimir():
    global conca, ran
    for i in range(1,16):
        ran = randint(1, 1001)
        conca+= str(ran) + ", "
    message1.value=conca
    conca=""
    for i in range(1,21):
        ran = randint(1, 1001)
        conca+= str(ran) + ", "
    message2.value=conca

app=App(title="ICI app")

button=PushButton(app,text="imprimir", command=imprimir)
message = Text(app, text="15 numeros del arbol")
message1= Text(app, text="")
espacio= Text(app, text="20 numeros del arbol")
message2= Text(app, text="")
app.display()