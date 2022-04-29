class employe:
    def __int__(self,emid,name,salary):
        self.emid=emid
        self.name=name
        self.salary=salary
    def display(self):
        print(self.emid,self.name,self.salary)