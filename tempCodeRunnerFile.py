self.queue2.append(x)
        while len(self.queue1)>0:
            self.queue2.append(self.queue1.pop(-1))
        print("Final queue: ",self.queue2)
        self.queue1, self.queue2 = self.queue2, self.queue1
        print(self.queue1)