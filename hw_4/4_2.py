# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging
import math
import time


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_type='thread'):
    step = (b - a) / n_iter
    part_iter = n_iter // n_jobs
    futures = []

    if executor_type == 'thread':
        executor_class = ThreadPoolExecutor
    else:
        executor_class = ProcessPoolExecutor

    with executor_class(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = a + i * part_iter * step
            end = start + part_iter * step
            if i == n_jobs - 1:  # Обработка последнего интервала
                end = b
            futures.append(executor.submit(integrate_part, f, start, end, step))

    return sum(future.result() for future in futures)



def integrate_part(f, start, end, step):
    logging.info(f"Запуск задачи: integrate_part с интервалом от {start} до {end}")
    acc = 0
    while start < end:
        acc += f(start) * step
        start += step
    logging.info(f"Завершение задачи: integrate_part с результатом {acc}")
    return acc


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='artifacts/4_2/integrate_logs.txt', filemode='w')
    cpu_num = 16
    for executor_type in ['thread', 'process']:
        times = []
        for n_jobs in range(1, cpu_num * 2 + 1):
            start_time = time.time()
            result = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_type=executor_type)
            end_time = time.time()
            times.append((n_jobs, end_time - start_time))
            logging.info(
                f"{executor_type.capitalize()}PoolExecutor with {n_jobs} jobs took {end_time - start_time} seconds.")

        # Запись результатов в файл
        with open(f"artifacts/4_2/integrate_times_{executor_type}.txt", "w") as f:
            for n_jobs, exec_time in times:
                f.write(f"{n_jobs} jobs: {exec_time} seconds\n")