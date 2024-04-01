import multiprocessing
import time
from codecs import encode

def process_a(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message == "exit":
            output_queue.put("exit")
            break
        output_queue.put(message.lower())
        time.sleep(5)

def process_b(input_queue, conn):
    while True:
        message = input_queue.get()
        if message == "exit":
            conn.send("exit")
            break
        encoded_message = encode(message, 'rot_13')
        conn.send(encoded_message)

if __name__ == "__main__":
    queue_a_b = multiprocessing.Queue()
    queue_main_a = multiprocessing.Queue()
    parent_conn, child_conn = multiprocessing.Pipe()

    process_a_proc = multiprocessing.Process(target=process_a, args=(queue_main_a, queue_a_b))
    process_b_proc = multiprocessing.Process(target=process_b, args=(queue_a_b, child_conn))

    process_a_proc.start()
    process_b_proc.start()

    with open("artifacts/4_3/interaction_log.txt", "a") as log_file:
        while True:
            message = input("Введите сообщение ('exit' чтобы выйти из программы): ")
            send_time = time.strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"{send_time} - Отправлено: {message}\n")

            if message == "exit":
                queue_main_a.put(message)
                break
            queue_main_a.put(message)

            encoded_message = parent_conn.recv()
            recv_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f"Закодированное сообщение: {encoded_message}")
            log_file.write(f"{recv_time} - Получено: {encoded_message}\n")

    process_a_proc.join()
    process_b_proc.join()
