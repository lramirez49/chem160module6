class waffler:
    def __init__(self,Nactors,myid):
        self.Nactors=Nactors
        self.myid=myid
        self.name="waffler"
        self.responses=["Cooperate","Defect"]
        self.next=1
    def response(self, other):
        self.next=(self.next+1)%2
        return self.responses[self.next]
    def inform(self, other, other_response):
        return
### Strategies available ###
strats=[defect,cooperate,tit_for_tat,coin_flip,biased_random,susp_tit_for_tat,grudger, waffler]
### Set list for the number of each strategy ###
Nactor_list=[5, 15, 20, 10, 10, 10, 10, 10]