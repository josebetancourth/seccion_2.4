import pywhatkit
import pandas as pd
import math
bd = pd.read_excel('celus.xlsx')
celus = bd['celular'].values
name = bd['nombres'].values
apellido = bd['apellidos'].values
video = "https://youtu.be/bj2-QytEjLI"
formulario = "https://forms.gle/MZs7Am7dThcGSfPx7"

x=0

for numero in celus:
  mensaje = """
  Hola %s, Te habla tu formador de misión TIC, si deseas recibir ayuda con la realizacion del formulario por que tienes algun problema responde este mensaje con la palabra AUTORIZO, o tambien puedes apoyarte en el video y formulario
  video=%s
  formulario=%s
  
  """% (name[x],video,formulario)
  if not pd.isna(numero):w
  
    celular = "+57"+str(numero)
    print("enviado a: %s %s"%(celular,name[x]))
    x+=1
    pywhatkit.sendwhatmsg_instantly(celular, mensaje, 15, True, 4)

print("enviados:%s"% x)

