# -*- coding: utf-8 -*-
import time
from threading import Thread
from multiprocessing import Process

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    # Синхронное выполнение
    start_time = time.time()
    for i in range(10):
        fibonacci(30)
    end_time = time.time()
    sync_time = end_time - start_time
    print(f"Синхронное выполнение: {sync_time} секунд")

    # Выполнение с использованием потоков
    start_time = time.time()
    threads = []
    for i in range(10):
        thread = Thread(target=fibonacci, args=(30,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    threads_time = end_time - start_time
    print(f"Выполнение с использованием потоков: {threads_time} секунд")

    # Выполнение с использованием процессов
    start_time = time.time()
    processes = []
    for i in range(10):
        process = Process(target=fibonacci, args=(30,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end_time = time.time()
    processes_time = end_time - start_time
    print(f"Выполнение с использованием процессов: {processes_time} секунд")

    # Запись результатов в файл
    results = f"""
    Синхронное выполнение: {sync_time} секунд
    Выполнение с использованием потоков: {threads_time} секунд
    Выполнение с использованием процессов: {processes_time} секунд
    """

    with open("artifacts/4_1/4_1.txt", "w") as file:
        file.write(results)
