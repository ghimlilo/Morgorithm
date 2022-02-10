from concurrent.futures import thread
import logging
import threading
import time


def thread_func(name):
    logging.info("[Sub-Thread] %s : 시작합니다.", name)
    time.sleep(3)
    logging.info("[Sub-Thread] %s : 종료합니다.", name)


# 메인영역
if __name__ == "__main__" :
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("[Main-Thread] 쓰레드 시작 전")

    x = threading.Thread(target=thread_func, args=('A', ))

    logging.info("[Main-Thread] 쓰레드 시작 전")

    x.start()

    logging.info("[Main-Thread] 쓰레드 종료를 기다립니다.")

    x.join()

    logging.info("[Main-Thread] 프로그램을 종료합니다.")

