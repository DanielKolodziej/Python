import socket
 
def Main():
    host = "127.0.0.1"
    port = 8080
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()
'''
run from prompt
python -m mysocket 8000

Dump:
Connection from: ('127.0.0.1', 63253)
from connected  user: GET / HTTP/1.1
Host: 127.0.0.1:8080
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: keep-alive


sending: GET / HTTP/1.1
HOST: 127.0.0.1:8080
UPGRADE-INSECURE-REQUESTS: 1
ACCEPT: TEXT/HTML,APPLICATION/XHTML+XML,APPLICATION/XML;Q=0.9,*/*;Q=0.8
USER-AGENT: MOZILLA/5.0 (MACINTOSH; INTEL MAC OS X 10_12_5) APPLEWEBKIT/603.2.4 (KHTML, LIKE GECKO) VERSION/10.1.1 SAFARI/603.2.4
ACCEPT-LANGUAGE: EN-US
ACCEPT-ENCODING: GZIP, DEFLATE
CONNECTION: KEEP-ALIVE

'''
