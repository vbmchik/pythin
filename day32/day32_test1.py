from threading import Thread, Lock


class TestA():

    def __init__(self) -> None:
        self.a = 1

    def aplus(self):
        self.a = self.a + 1

    def run(self):
        l = [Thread(target=self.aplus) for _ in range(1000)]
        for k in l:
            k.start()
        for k in l:
            k.join()
        print(self.a)


t = TestA()
t.run()
