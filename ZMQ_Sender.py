from time import sleep
import time
import zmq
import cv2
import pafy
import youtube_dl
from multiprocessing import Process
context = zmq.Context()

def sender_1():

    socket = context.socket(zmq.PUSH)
    print('Binding to port 5555')
    socket.bind("tcp://*:5555")
    get_url = "https://www.youtube.com/watch?v=ORrrKXGx2SE"
    path = pafy.new(get_url).streams[-1]
    cap = cv2.VideoCapture(path.url)
    #fps = cap.get(cv2.CAP_PROP_FPS)
    #print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    sleep(1)
    print("server started")
    print(cap.isOpened())

    while (cap.isOpened()):
        print("Sending")
        ret, frame = cap.read()
        socket.send_pyobj(frame)

def sender_2():

    socket = context.socket(zmq.PUSH)
    print('Binding to port 4545')
    socket.bind("tcp://*:4545")
    get_url = "https://www.youtube.com/watch?v=CfhEWj9sd9A"
    path = pafy.new(get_url).streams[-1]
    cap = cv2.VideoCapture(path.url)
    sleep(1)
    print("server started")
    print(cap.isOpened())

    while (cap.isOpened()):
        print("Sending")
        ret, frame = cap.read()
        socket.send_pyobj(frame)



Process(target=sender_1).start()
Process(target=sender_2).start()
