from time import sleep
import time
import zmq
import cv2
from multiprocessing import Process
context = zmq.Context()


def receiver_1():
    print("client started")
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://localhost:5555")

    while True:
        start = time.time()
        image = socket.recv_pyobj()
        end = time.time()
        seconds = end - start
        fps = 1 / seconds
        fps_text = "FPS: {:.2f}".format(fps)
        cv2.putText(image, fps_text, (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.namedWindow("frame_1", cv2.WINDOW_AUTOSIZE)
        cv2.imshow('frame_1', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def receiver_2():
    print("client started")
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://localhost:4545")
    
    while True:
        start = time.time()
        image = socket.recv_pyobj()
        end = time.time()
        seconds = end - start
        fps = 1 / seconds
        fps_text = "FPS: {:.2f}".format(fps)
        cv2.putText(image, fps_text, (80, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('frame_2', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


Process(target=receiver_1).start()
Process(target=receiver_2).start()

