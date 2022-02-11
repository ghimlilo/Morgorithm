import logging, threading, time

start_time = time.time()

def work(name, start, end, result):
    logging.info("[Sub-Thread] %s : 시작합니다.", name)

    total = 0
    for i in range(start, end):
        total += i

    result.append(total)

    logging.info("[Sub-Thread] %s : 종료합니다.", name)

    return
    
    # logging.info("[Sub-Thread] %s : 결과", total)
    # logging.info("[Sub-Thread] %s : 종료합니다.", name)

if __name__ == "__main__":
    format = "%(asctime)s.%(msecs)03d : %(message)s"    # Logging format 설정
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    START, END = 0, 100000000
    result = list()
    
    th1 = threading.Thread(target=work, args=('A', START, END, result))

    logging.info("[Main-Thread] 쓰레드 시작 전")

    th1.start()
    th1.join()

    logging.info("[Main-Thread] 프로그램을 종료합니다.")

print("%s seconds" %(time.time() - start_time), f"몇대~~~몇! : {sum(result)}")
