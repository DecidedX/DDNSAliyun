from threading import Timer


class TimerTask:
    def __init__(self, interval, task):
        self.interval = interval
        self.task = task
        self.timer = None

    def loop_task(self):
        self.task()
        self.start()

    def start(self):
        self.timer = Timer(self.interval, self.loop_task)
        self.timer.start()

    def do_start(self):
        self.loop_task()

    def cancel(self):
        self.timer.cancel()

