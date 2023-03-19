from threading import  Timer


timer = Timer(interval=5, function=lambda: print("Timer thread started!"))
timer.start()