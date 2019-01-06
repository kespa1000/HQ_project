# This Python file uses the following encoding: utf-8
import socket
print('hi')
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET <= IPv4 , DGRAM <= UDP ���
# server
SERVER_IP = '192.168.56.1'
PORT = 10000

sock.bind((SERVER_IP, PORT))
# ����� ���� Port Open, �ڽ�IP , Port (����)
print("server start")
print("server ip: {:s} | port: {:d}".format(SERVER_IP, PORT))


while True:
    data, info = sock.recvfrom(65535)
    # Ŭ���̾�Ʈ���Լ� ���ڿ��� ���޹ޱ� ����.
    # data�� ���޹��� ���ڸ� �����ϱ� ���� ����, ���ڴ� �ִ� �� ����Ʈ ���� �������ΰ��� ���Ѱ�.
    # info���� ip�ּҿ� port ��ȣ�� �ް� ��� �����ʹ� Ʃ�÷� ����ȴ�.
    print('Client: {:s}/{:d}'.format(info[0], info[1]))
    print('echo data {:s}'.format(data.decode()))
    # ù��°�� decode�� encode�̴�. ���̽��� �⺻������ �����ڵ带 �����ϰ� �ִ�.
    # ������ �츮�� ��Ʈ��ũ������ ���ڸ� �ְ� ���������� bytes, bytearray Ÿ������ �ٲ��־�� �Ѵ�.
    # Client���� ���ڵ����͸� �����ٸ� bytes type���� �޽����� ���� �Ǵµ� ���� �޽����� ���̽㿡��
    # ����ϰ� �ʹٸ� �������ڿ�.decode()�� ���� decoding ���־���ϰ� ���� ���� ���ڿ��� �ִٸ�
    #  ���� ���ڿ�.encoding()�� ���־�� �Ѵ�.
    # -> Socket �� ���� data format : byte or bytearray , python I/O data format�� �°� decoding, encoding

    sock.sendto(data, info)
    # �ι�°�� send() �� sendto() �� �����Դϴ�. send() �޼���� �⺻������ ���ϴ� ip�� �����͸� ������ ����
    # -> send()�� TCP���̰� sendto()�� UDP�� �Դϴ�.
    # send()�� ������ ���� �� ����Ʈ ���� �����ϸ�, ����� ��� buffer_size�� ������ ���� �� ��쿡��
    # ���������� ���̳��ϴ�. ������ sendto()�� ��쿡�� ������ �� ���۸� ������ �����ߴ��� ���ο�
    #  ���� ������ ��� ���۸� ��� �����ϴ�.
