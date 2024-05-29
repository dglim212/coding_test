class fibonacci:
    def __init__(self, n:int):
        self.fibonacci_dict = {}
        self.iter = 0
        self.n = n
        
        self.fibonacci_forward()
        print(self.fibonacci_dict[n][0],self.fibonacci_dict[n][1])
    def fibonacci_forward(self):
        i = self.iter
        if i == 0:
            self.fibonacci_dict[i] = [1,0]
        elif i == 1:
            self.fibonacci_dict[i] = [0,1]
        else:
            f0 = self.fibonacci_dict[i-1][0] + self.fibonacci_dict[i-2][0]
            f1 = self.fibonacci_dict[i-1][1] + self.fibonacci_dict[i-2][1]
            self.fibonacci_dict[i] = [f0,f1]
        self.iter += 1
        if self.iter < self.n+1:
            self.fibonacci_forward()
            
T = int(input())
for i in range(T):
    n = int(input())
    fibonacci(n)
    