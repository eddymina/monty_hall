import numpy as np 
import matplotlib.pyplot as plt 
import random

class Monty_Hall:
    """
    Monty Hall class 
    """
    def __init__(self,niters=1000,verbose=False):
        #TO DO Introduce support for n doors 
        
        self.niters= niters #define number of iterations 
        self.verbose=verbose #print game results per iteration 
        self.swap_good,self.keep_good=[],[] #success rates 
        
    def round1(self):
        """
        In the first round
        you define a prize winning 
        door index and a index (door) 
        that the user choose
        """
        states = np.array([0,0,0]) #set states to 0 
        
        options=[0,1,2]
        prize_ind = random.choice(options) #set gold door index 
        states[prize_ind]=1 
        choice=random.choice(options) #set choice set by user (unrestricted )

        if self.verbose: print('Prize location:: {} | User choice:: {} | States:: {}'.format(prize_ind+1,choice+1,states))    
        return states,choice
    
    def door2remove(self,states,choice):
        """
        At the beginning of the second round
        a door must be removed that is not 
        the door that the user selected 
        and is not a prize door. 
        """
        same= True
        while same: #check that choice != door removed 
            remove=random.choice(np.argwhere(states==0).flatten()) #asserting non prize door selected 
            if  remove == choice:
                same=True
            else:
                same=False
        if self.verbose: print('Removing door::',remove+1)
        return remove
    
    
    def round2_swap(self,remove,choice):
        """
        Chooising the index that is not 
        the door you selected nor the 
        door that was removed
        """
        options=[0,1,2]
        options.remove(remove)
        options.remove(choice)
        return options[0]

    
    def check(self,selected,states):
        """
        Check if the final decision matches
        the location of the prize door. 
        """
        if selected == np.argwhere(states==1).flatten():
            return True
        else:
            return False  
        
    def compute(self):
        """
        Computer over n number of iterations
        and see the success rate smoothed 
        """
        
        swap_g,keep_g=0,0
        for i in range(self.niters):
            if self.verbose: print('\nIter {}---------------------'.format(i))
            s,c = self.round1()
            r=self.door2remove(s,c)
            sel_swp= self.round2_swap(r,c)
            sel_keep = c

            if self.verbose: print('Swap door::{} | Keep door::{}'.format(sel_swp+1,sel_keep+1))
            if self.check(sel_swp,s):
                if self.verbose: print('Swapping was a good choice')
                self.swap_good.append(1)
                self.keep_good.append(0)
            elif self.check(sel_keep,s):
                self.keep_good.append(1)
                self.swap_good.append(0)
                if self.verbose: print('Keeping was good choice')
            else:
                raise ValueError('Something Weird Is going on')

        if self.verbose: print('##Computations Done##')
            
    def plot_res(self):
        """
        Plotting the cummulative success rate 
        over the number of games 
        """
        plt.figure(figsize=(10,5))
        plt.xlabel('Iters')
        plt.ylabel('Cumulative Succes Rate')
        
        if len(self.swap_good)==0:
            raise ValueError('Please Run Monty_Hall(*args).compute() first')
            
        self.res_swapping= np.cumsum(self.swap_good)/self.niters
        plt.plot(np.arange(self.niters),self.res_swapping,label='Swapping Is Good')
        self.res_keeping= np.cumsum(self.keep_good)/self.niters
        plt.plot(np.arange(self.niters),self.res_keeping,label='Keeping Is Good')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    mh=Monty_Hall(niters=7plt00,verbose=True)
    mh.compute()
    mh.plot_res()

