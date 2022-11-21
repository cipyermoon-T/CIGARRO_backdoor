import os
import time

path = r"C:\\RiotGames\\"

def createPath(path):
   if not os.path.isdir(path):
      os.makedirs(path)

def installFile(path,filename):
   file = open(filename,"r")
   newFile = open(path+filename,"w")

   for lines in file:
      newFile.write(lines)
   newFile.close()
   file.close()

def installAll(path):
   files = os.listdir()
   for file in files:
      installFile(path,file)

def start():
   os.startfile("C:\\RiotGames\\instalarRegistro.bat")
   os.startfile("C:\\RiotGames\\executar.bat")

createPath(path)
installAll(path)
start()
