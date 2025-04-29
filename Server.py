import socket
import threading
import dframe as df
from threading import Thread
from dframe import *

lock = threading.Lock()

def client_thread(connection):
    data = connection.recv(1024)  
    log = (data.decode()).split(' ')
    log[0] = int(log[0])
    
    voter_status = df.verify(log[0], log[1])  
    
    if voter_status is True:
        if df.isEligible(log[0]):
            print('Invalid Voter')
            connection.send("Authenticate".encode())
        else:
            print('Vote Already Cast by ID:' + str(log[0]))
            connection.send("VoteCasted".encode())
    
    elif voter_status == 'WrongPassword':  
        print('Wrong Password Entered for ID:' + str(log[0]))
        connection.send("WrongPassword".encode())        

    else:
        print('Voter Logged in... ID:' + str(log[0]))
        connection.send("InvalidVoter".encode())


    data = connection.recv(1024)                                    
    print("Vote Received from ID: "+str(log[0])+"  Processing...")
    lock.acquire()
    #update Database
    if(df.vote_update(data.decode(),log[0])):
        print("Vote Casted Sucessfully by voter ID = "+str(log[0]))
        connection.send("Successful".encode())
    else:
        print("Vote Update Failed by voter ID = "+str(log[0]))
        connection.send("Vote Update Failed".encode())
                                                                       

    lock.release()
    connection.close()


def voting_Server():

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send("Connection Established".encode())   
        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    voting_Server()
