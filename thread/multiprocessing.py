import logging, time
from multiprocess import Process, Queue

start_time = time.time()

def work(name, start, end, result):
    logging.info("[Sub-Thread] %s : 시작합니다.", name)

    total = 0
    for i in range(start, end):
        total += i
    result.put(total)

    logging.info("[Sub-Thread] %s : 종료합니다.", name)

    return

if __name__ == "__main__":
    format = "%(asctime)s.%(msecs)03d : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    START, END = 0, 100000000
    result = Queue()
    
    th1 = Process(target=work, args=('A', START, END//2, result))
    th2 = Process(target=work, args=('B', END//2, END, result))

    logging.info("[Main-Thread] 쓰레드 시작 전")

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    logging.info("[Main-Thread] 프로그램을 종료합니다.")

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp

    print("%s seconds" %(time.time() - start_time), f"몇대~~~몇! : {total}")
    logging.info("[Main-Thread] 프로그램을 종료합니다.")