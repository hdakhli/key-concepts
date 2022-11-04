import time
from multiprocessing import Pool


def call_function(user_name):
    time.sleep(0.1)
    print(f"Call from process user: {user_name}")


if __name__ == '__main__':
    start_time = time.time()
    users = []
    for user_id in range(1, 15):
        users.append(user_id)

    for user in users:
        call_function(user)
    # pool = Pool(6)
    # pool.map(call_function, users)

    end_time = time.time()
    duration = end_time - start_time
    print(f"Duration: {duration}")
