class Teammember:
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
class Worker:
    def __init__(self,pay,jobtitle):
        self.pay=pay
        self.jobtitle=jobtitle
class TeamLeader(Teammember,Worker):
    def __init__(self,name,uid,pay,jobtitle,exp):
        self.exp=exp
        Teammember.__init__(self,name,uid)
        Worker.__init__(self,pay,jobtitle)
        print("Name:{},Pay:{},Exp:{}".format(self.name,self.pay,self.exp))
TL=TeamLeader('Jake',10001,250000,'Scrum Master',5)
print(TeamLeader.mro())