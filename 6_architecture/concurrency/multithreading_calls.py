from threading import Thread
import time


def call_function(user_name):
    time.sleep(0.2)
    print(f"Call from thread user: {user_name}\n")


if __name__ == '__main__':
    start_time = time.time()
    users = []
    for user_id in range(1, 15):
        users.append(user_id)

    # creating threads
    threads = []
    for user in users:
        th = Thread(target=call_function, args=(user,))
        th.start()
        threads.append(th)

    # check the end of all threads
    for th in threads:
        th.join()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Duration: {duration}")
