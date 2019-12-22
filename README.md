# Monty Hall Problem 

The Monty Hall problem has always been something that has challenged me intuitively so I decided to tackle it from a pythonic point of view. In this repo I made a simple `Monty_Hall` class with simple code the expresses the unique statistic nature of this problem. Below is a simple explanation of the problem:

```
Explanation:

Suppose you are on a game show and there are 3 doors. Behind two of the doors are goats and the remainder 3rd door had some gold.\n There are two rounds to this game. In the first round, you must pick on of the 3 doors as your choice. Here your probability of\n picking a gold behind a door is 1/3 and a goat is 2/3. Following, your choice, the game show host removes on of the known doors that has a goat behind it. (It is assumed here that the game show host always removes a goat door because he/she knowns whats behind it). Following that you enter the second round where there are two doors that remain:: the door you initially selected and the other mystery door. Should you keep your choice or swap your choice to the other door?


Solution:

Because there are only two doors remaining in the second round, it is tempting to think you have a 50/50 chance at selecting the right door in the second round, but it isn't true- you cannot discount the first round. As we agreed before the first round each door has a 1/3 probability. Looking at it another way for a door your select in the first round, no matter what your chance (of success) will remain 1/3. Even if 100 doors were added after, because of your initial circumstances, your probability is 1/3. Going back to the first round, for every other door you select, your success rate is 1/3 and remainder doors are 2/3 (1/3 + 1/3). But you cannot choose door at once! Monty makes that easy by removing one of the doors with a goat. As such, switching your decision is ~2/3 or approximately 2x better than keeping your decision!
```
---

#### Using Repo: 
- `git clone https://github.com/eddymina/monty_hall`

```python
from monty import Monty_Hall 
mh=Monty_Hall(niters=2,verbose=True) #set the number of iterations and print results (verbose is False)
## Set niters>700 to to smooth out noise 
## Might want to set verbose to false too! 
mh.compute() #
mh.plot_res() #compute() is needed prior to plot results 
```
```
--------------------
Prize location:: 2 | User choice:: 1 | States:: [0 1 0]
Removing door:: 3
Swap door::2 | Keep door::1
Swapping was a good choice

Iter 1---------------------
Prize location:: 2 | User choice:: 2 | States:: [0 1 0]
Removing door:: 3
Swap door::1 | Keep door::2
Keeping was good choice
##Computations Done##
```
---

#### Methodology 
```
1. Randomly choose a prize location and define state. (EX: [0 1 0], prize is at location 2 (index 1))
2. Remove a door that has a goat and is not the door your selected (obviously)
3. Allow user to swap and keep choice 
4. Compute Cumulative Success Rate:
	For an iteration:	
		success_keeping == 1 else it is 0 
		success_swapping == 1 else it is 0 

5. For all iterations sum the successes
6. Plot Results 
```




