# This Python file uses the following encoding: utf-8
import socket
print('hi')
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET <= IPv4 , DGRAM <= UDP 방식
# server
SERVER_IP = '192.168.56.1'
PORT = 10000

sock.bind((SERVER_IP, PORT))
# 통신을 위해 Port Open, 자신IP , Port (임의)
print("server start")
print("server ip: {:s} | port: {:d}".format(SERVER_IP, PORT))


while True:
    data, info = sock.recvfrom(65535)
    # 클라이언트에게서 문자열을 전달받기 위함.
    # data는 전달받은 문자를 저장하기 위한 변수, 인자는 최대 몇 바이트 까지 받을것인가에 대한것.
    # info에는 ip주소와 port 번호를 받고 모든 데이터는 튜플로 저장된다.
    print('Client: {:s}/{:d}'.format(info[0], info[1]))
    print('echo data {:s}'.format(data.decode()))
    # 첫번째는 decode와 encode이다. 파이썬은 기본적으로 유니코드를 지원하고 있다.
    # 하지만 우리가 네트워크상으로 문자를 주고 받을때에는 bytes, bytearray 타입으로 바꿔주어야 한다.
    # Client에서 문자데이터를 보낸다면 bytes type으로 메시지가 오게 되는데 받은 메시지를 파이썬에서
    # 출력하고 싶다면 받은문자열.decode()를 통해 decoding 해주어야하고 만약 보낼 문자열이 있다면
    #  보낼 문자열.encoding()을 해주어야 한다.
    # -> Socket 상 전달 data format : byte or bytearray , python I/O data format에 맞게 decoding, encoding

    sock.sendto(data, info)
    # 두번째는 send() 와 sendto() 의 차이입니다. send() 메서드는 기본적으로 원하는 ip에 데이터를 보내는 역할
    # -> send()는 TCP용이고 sendto()는 UDP용 입니다.
    # send()는 서버에 전송 된 바이트 수를 추적하며, 명령은 모든 buffer_size가 서버에 수신 된 경우에만
    # 성공적으로 끝이납니다. 하지만 sendto()의 경우에는 서버가 이 버퍼를 실제로 수신했는지 여부에
    #  대한 정보가 없어도 버퍼를 대상에 보냅니다.
