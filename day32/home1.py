from datetime import datetime
from threading import Thread
from time import sleep


class MyOwnThread(Thread):
    
    def __init__(self, filename, n):
        Thread.__init__(self)
        self.filename = filename
        self.wordcount = {}
        self.n = n

    def run(self) -> None:
        print(f"start thread {self.n}")
        with open(self.filename, "r") as shfile:
            text = shfile.read().lower()
        text = self.clearword(text)
        text = list(filter(lambda x: x != '', text.split(" ")))
        self.countWords(text)
        print(f"file {self.filename} words = {len(self.wordcount)}")

     
    def clearword(self, word):
        cleanword = ''.join([x for x in word if x.isalpha() or x == ' '])
        return cleanword
    
    def countWords(self, text: str):
        self.wordcount = {}
        for word in text:
            if not word in self.wordcount:
                self.wordcount[word] = 1
            else:
                self.wordcount[word] += 1


#print(datetime.now())
#threader = []
#for i in range(30):
#    threader.append(MyOwnThread("advs.txt", i))
#for i in range(30):
#    threader[i].start()
#for i in range(30):
#    threader[i].join()



#print(datetime.now())
#print(threader[0].wordcount["dog"])
