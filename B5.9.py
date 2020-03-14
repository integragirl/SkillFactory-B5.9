def time_this(NUM_RUNS):
    
    class TimeDec:
        
        def __init__(self):
            self.start = 0
            self.end = 0
            self.sum_time = 0
            self.avg_time = 0
            self.NUM_RUNS = 0
            
        def __enter__(self):
            return self
        
        def __exit__(self, type, value, traceback):
            self.avg_time = self.sum_time / NUM_RUNS
            print(self)
            
        def time_start(self):
            import time
            self.start = time.time()
            self.NUM_RUNS += 1
            
        def time_end(self):
            import time
            self.end = time.time()
            self.sum_time += (self.end - self.start)
            
        def __str__(self):
            return "Выполнение заняло %.5f секунд" % self.avg_time
    
    def decorator(func):
        def wrap():
            with TimeDec() as TD:
                for _ in range(NUM_RUNS):
                    TD.time_start()
                    func()
                    TD.time_end()
        return wrap
    return decorator

@time_this(10)
def f():
    for j in range(1000000):
        pass
    
f()