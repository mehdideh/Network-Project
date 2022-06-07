from socket import *
try:
 server_name="2.tcp.eu.ngrok.io"
 server_port=14288
 clientsocket=socket(AF_INET,SOCK_STREAM)
 clientsocket.connect((server_name,server_port))
except:
 print("connection with server and client failure:((")
print("1-HELP")
print("2-LIST")
print("3-PWD")
print("4-(dirname) MKDIR")
print("5-(dirname) RMDIR")
print("6-(dirname) CD")
print("7-(filename) DOWNLOAD")
print("9-EXIT")
while (True):
  dastoor=input("\n \nenter your command :  ")
  if(dastoor=="EXIT"):
     print("The connection to the server was disconnected and the program ended :)")
     break
  elif(dastoor=="HELP"):
     print("HELP :   list of known commands")
     print("LIST :   ")
     print("PWD :   Return the pathname of the current directory on the server")
     print("(dirname) MKDIR :   Create a new directory on the server")
     print("(dirname) RMDIR :   Remove the directory named dirname on the server")
     print("(dirname) CD :   Set the current directory on the server")
     print("(filename) DOWNLOAD :   download file from server")
     continue
  elif (dastoor == "LIST"):
    clientsocket.send(dastoor.encode())
    listdastoorat = clientsocket.recv(1024).decode()
    print(listdastoorat)
    continue
  elif (dastoor == "PWD"):
    clientsocket.send(dastoor.encode())
    listdastoorat = clientsocket.recv(1024)
    print(listdastoorat.decode())
    continue
  elif ("MKDIR" in dastoor):
    clientsocket.send(dastoor.encode())
    listdastoorat = clientsocket.recv(1024)
    print(listdastoorat.decode())
    continue
  elif ("RMDIR" in dastoor):
    clientsocket.send(dastoor.encode())
    listdastoorat = clientsocket.recv(1024)
    print(listdastoorat.decode())
    continue
  elif ("CD" in dastoor):
    clientsocket.send(dastoor.encode())
    listdastoorat = clientsocket.recv(1024)
    print(listdastoorat.decode())
    continue
  elif ("DOWNLOAD" in dastoor):
      clientsocket.send(dastoor.encode())
      server_portT = int(clientsocket.recv(1024).decode())
      if(server_portT==404):
          print("Error 404!!!\nFile not found\n")
      else:
       server_nameE = "127.0.0.1"
       data = b""
       clientsocketT = socket(AF_INET, SOCK_STREAM)
       clientsocketT.connect((server_nameE, server_portT))
       download_data = clientsocketT.recv(1048576)
       data += download_data
       with open(dastoor.split(' ')[0], 'wb') as file:
        file.write(data)
       print(" Downloaded successfully :)")
       clientsocketT.close()
  else:
     print("erorr!!  your command not found")

