import torch
from torch import nn

class mod(nn.Module):

    #I hope this model is good
    #Conv2d with one hot encoding does better than Conv1d

    def __init__(self):
        super().__init__()
        #input :2d(one hot) : 53*20
        self.c1 = nn.Conv2d(1 , 3 , 4 , stride = 1 , padding = 0)
        #c1 = 50 * 17 , after maxpool = 12  , 4
        self.c2 = nn.Conv2d(3 , 6 , 2 , stride = 1 , padding = 1)
        #c2 = 13* 5  , after maxpool = 6  , 2
        self.c3 = nn.Conv2d(6 , 15 , 3 , stride = 3 , padding = 1 ) #c2 = 2* 1  
        self.sig = nn.Sigmoid()
        self.maxpool = nn.MaxPool2d(4 , 4)
        self.maxpool2 = nn.MaxPool2d(2 , 2)
        self.l1 = nn.Linear(30 , 10)
        self.l2 = nn.Linear(10 ,  2)

    def forward(self, x):
        x =  self.sig(self.c1(x))
        x = self.maxpool(x)
        x = self.sig(self.c2(x))
        x = self.maxpool2(x)
        x = self.sig(self.c3(x))

        x = x.view(-1 ,30 )

        x = self.sig(self.l1(x))
        x = self.sig(self.l2(x))

        return  (x)


class mod2(nn.Module):

#USING LSTM
    def __init__(self):
        super().__init__()

        self.lstm = nn.LSTM(53 , 4)
        self.l1 = nn.Linear(80 , 40)
        self.l2 = nn.Linear(40 , 10)
        self.l3  = nn.Linear(10 , 2)

        self.act = nn.Sigmoid()
        self.inneract = nn.Tanh()

    def forward(self, x):

        x = x.view(20 , 1 , 53)
        x , y = self.lstm(x) 
        x = x.view(1 , -1)

        x = self.inneract(self.l1(x))
        x = self.inneract(self.l2(x))
        x = self.l3(x)

        return x
