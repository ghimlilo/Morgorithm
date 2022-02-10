import logging
import threading
import time

# thread에서 실행할 함수
def work(name):
    logging.info("[44444]")
    logging.info("[Sub-Thread] %s : 시작합니다.", name)
    logging.info("[55555]")
    time.sleep(3)
    logging.info("[Sub-Thread] %s : 종료합니다.", name)

# main 영역
if __name__ == "__main__" :     # main thread 흐름을 타는 시작점
    format = "%(asctime)s : %(message)s"    # Logging format 설정
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    logging.info("[11111]")

    x = threading.Thread(target=work, args=('A', ))

    logging.info("[22222]")

    logging.info("[Main-Thread] 쓰레드 시작 전")

    logging.info("[33333]")

    x.start()   # sub thread 시작

    logging.info("[66666]")

    logging.info("[Main-Thread] 프로그램을 종료합니다.")

    logging.info("[77777]")

