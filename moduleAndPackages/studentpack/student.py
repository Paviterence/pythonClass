class student:
    def __int__(self,sid,sname,grade):
        self.employeid=sid
        self.emplyeename=sname
        self.salary=grade
    def display(self):
        print(self.employeid,self.emplyeename,self.salary)