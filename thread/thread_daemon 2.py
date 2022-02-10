import logging
import threading
import time


def work(name, d) :
    logging.info("[Sub-Thread] %s : 시작합니다.", name)

    for i in d:
        print(i)

    logging.info("[Sub-Thread] %s : 종료합니다.", name)


if __name__ == "__main__" : 

    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    x = threading.Thread(target=work, args=('A', range(100)), daemon=True)
    # y = threading.Thread(target=work, args=('B', range(100)), daemon=True)

    logging.info("[Main-Thread] 쓰레드 실행 전")


    x.start()
    # y.start()
    # x.join()
    # y.join()

    logging.info("[Main-Thread] 프로그램을 종료합니다.")