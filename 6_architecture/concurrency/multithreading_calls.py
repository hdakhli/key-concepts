import time


def call_function(user_name):
    time.sleep(0.2)
    print(f"Call from thread user: {user_name}\n")


if __name__ == '__main__':
    start_time = time.time()
    users = []
    for user_id in range(1, 16):
        users.append(user_id)

    for user in users:
        call_function(user)

    end_time = time.time()
    duration = end_time - start_time
    print(f"Duration: {duration}")
