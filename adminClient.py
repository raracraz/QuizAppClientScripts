import socket, sys
import uuid
import base64
import os
import glob


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 23))

def downloadFile(tableName, colName, localrowid):
    '''
    Purpose of this function is to download the files from the server to the client
    '''
    #get the file from the server
    
    #decode the file
    #get all files from a directory
    file = ''
    while True:
        file = s.recv(1024)
        file = (file).decode('utf-8')
        #open the file to write
        with open(file, 'wb') as f:
            f.write(file.encode('utf-8'))
            #print the file downloaded
        print('\nFile downloaded successfully.')
        # if no more files to download break
        if file == 'end':
            break


#Function to upload the files to the server
def uploadFile(filename, localrowid):
    '''
    Purpose of this function is to upload the files to the server
    '''
    #open the file to read
    with open(filename, 'rb') as f:
        #read the file
        file = f.read()
    #encode the file
    file = base64.b64encode(file)
    #send the file to the server
    s.send(file)
    #print the file uploaded
    print('\nFile uploaded successfully.\n')



while True:

    msg = input("msg to send ['q' to quit]=> ")
    obuf = base64.b64encode(str(msg).encode()) # convert msg string to bytes
    ret=s.send(obuf)
    #print("{} byte(s) have sent".format(ret))
    if msg == '1':
        downloadFile('questions', 'questions', '')
        print('\n')
    if (msg == 'q'):
        s.close()
        break  
    else:
        ibuf = s.recv(255)
    if len(ibuf) > 0:
        print(ibuf.decode())
    else:
        print("The connection has dropped")
        break
print("Bye Bye")