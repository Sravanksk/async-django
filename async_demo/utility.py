from time import sleep


def sleep_and_run_task(secs):
    sleep(secs)
    print('Task Executed after', secs, 'sec!')
