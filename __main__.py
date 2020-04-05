from Monitor import Monitor
from GetData import get_data
from PutData import put_data


def __main__():
    monitor = Monitor()
    time = 0
    while True:
        time += 1
        cur_request = get_data(time)
        (cur_action, debug_str) = monitor.analyze_request(cur_request)
        put_data(cur_action, debug_str)


if __name__ == '__main__':
    __main__()
