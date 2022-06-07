from  socket import *
import random
import os
server_port=2121
serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind(('127.0.0.1',server_port))
serversocket.listen(5)
print("server is ready to recieve")
connectionsocket,addr=serversocket.accept()
while True:
    dastoor=connectionsocket.recv(1024).decode()
    if(dastoor=="PWD"):
        cwd = os.getcwd()
        jomleh=(f"current working directory:{cwd}")
        connectionsocket.send(jomleh.encode())
    elif (dastoor == "LIST"):
        listt = os.listdir()
        listtt=""
        sum=0
        j=0
        cwd = os.getcwd()
        for i in listt:
          path = os.path.join(cwd, i)
          if(os.path.isdir(path)):
             listtt+=">"
             for path, dirs, files in os.walk(path):
                 for f in files:
                     fp = os.path.join(path, f)
                     j += os.path.getsize(fp)
          else:
            j=os.path.getsize(path)

          listtt+=f"{i} : {j} BYTES \n"
          sum=sum+j
        listtt+=f"sum size of files:{sum} BYTES"
        connectionsocket.send(listtt.encode())
    elif (dastoor.split(' ')[1]=="MKDIR"):
        directory_name=dastoor.split(' ')[0]
        cwd = os.getcwd()
        path = os.path.join(cwd, directory_name)
        os.makedirs(path)
        jomleh = ("your directory was secussefully created ")
        connectionsocket.send(jomleh.encode())
    elif (dastoor.split(' ')[1] == "RMDIR"):
        directory_name = dastoor.split(' ')[0]
        cwd = os.getcwd()
        path = os.path.join(cwd, directory_name)
        listt = os.listdir()
        flag = 0
        for i in listt:
            if (i == directory_name):
                flag = 1
                os.rmdir(path)
                jomleh = ("your directory was secussefully deleted :)")
                break
        if (flag == 0):
            jomleh = ("your directory was not found :(")
        connectionsocket.send(jomleh.encode())
    elif (dastoor.split(' ')[1] == "CD"):
        directory_name = dastoor.split(' ')[0]
        path=os.getcwd()
        path = os.path.join(path, directory_name)
        cwd = os.listdir()
        flag=0
        if(directory_name=="../"):
            if(os.path.basename(os.getcwd())!="server"):
             os.chdir('../')
             jomleh = ("your directory was secussefully change:)")
            else:
              jomleh=("eror!!!! You do not have permission to access this folder")
        else:
         for i in cwd:
            if(i==directory_name):
                 flag=1
                 os.chdir(path)
                 jomleh = ("your directory was secussefully change:)")
                 break
         if(flag==0):
            jomleh=("your directory was not found :(")
        connectionsocket.send(jomleh.encode())
    elif (dastoor.split(' ')[1] == "DOWNLOAD"):
        file_name = dastoor.split(' ')[0]
        if os.path.exists(file_name):
            server_portT = random.randrange(3000, 5000)
            connectionsocket.send(str(server_portT).encode())
            serversocketT = socket(AF_INET, SOCK_STREAM)
            serversocketT.bind(('127.0.0.1', server_portT))
            serversocketT.listen(5)
            connectionsocketT, addr = serversocketT.accept()
            print("Download started...")
            with open(file_name, 'rb') as f:
                data = f.read()
                connectionsocketT.send(data)
                connectionsocketT.close()
                print("Download completed")
        else:
            print("Bad request!!!")
            ptr = "404"
            connectionsocket.send(ptr.encode())

connectionsocket.close()