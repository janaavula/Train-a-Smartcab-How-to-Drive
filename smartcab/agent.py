import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator



class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""
    
    
   
    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        self.actionvalue = 0
        self.iteration = 0
        self.q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.numberoftrails = numberoftrails
        self.resetvalue = 0
        self.deadline2 = []
        self.rewards = []
        
        

    def reset(self, destination=None):
        self.planner.route_to(destination)
         # TODO: Prepare for a new trip; reset any variables here, if required
        global deadline1, destinationreached, deadlines
        
        
        if self.resetvalue > 0:
            if self.numberoftrails > deadline1: 
                destinationvalue = 0
            else:
                destinationvalue = 1
            #reset values
            destinationreached.append(destinationvalue)
            self.deadline2[:] = []
            #print self.allrewards
            #print "sum %d" % sum(self.rewards)
            allrewards.append(sum(rewards))
            alldeadlines.append(deadlines)
            rewards[:] = []
            deadlines = 0
            self.numberoftrails = 0
        
        
        
       
       
       
    
    def update(self, t):
        # Gather inputs
        global deadline1, deadlines
        
        #self.actionvalue = 0
        countvalues = 0
        self.resetvalue = 1
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)
        self.deadline2.append(deadline)
        deadline1 = max(self.deadline2)

        #Below code is for making the first iteration has previous state, action and reward so that we can use it in Q function
        #as Q function requires both current state and associate action of that state and future state and associated 
        #action of that state.
        if self.iteration == 0:
            self.state = (inputs['light'], inputs['oncoming'], inputs['left'],inputs['right'],self.next_waypoint,deadline)
            self.previousstate = self.state
            self.previousaction = random.choice([None, 'forward', 'left', 'right'])
            key = (self.previousstate,self.previousaction)
            self.reward = self.env.act(self, self.previousaction)
            self.iteration = 1
            self.numberoftrails = self.numberoftrails+1
            self.totalreward = 0
        
        #The below iterations holds next state as future state.
        if self.iteration == 1:
                self.state = (inputs['light'], inputs['oncoming'], inputs['left'],inputs['right'],self.next_waypoint)
                self.nextstate = self.state
                #print self.nextstate
                actionlist = [None, 'forward', 'left', 'right']
                values = {}
                actionqlist =[]
                # if Q table is not empty we will go through below flow, if Q table is empty we will go with else functionality
                #and pick a random action as Q table is empty and there is no state and action value available.
                
                if len(self.q):
                    #going through Q table to check if the state exists, if state exists pick action with maximum value
                    
                    for k,v in self.q.iteritems():
                        #if v != 0:
                        #print k,v
                        if k[0] == self.state:
                            #put the values in v dictiornaty where key is action and value is associated value in q table                                   #for that state and action, if not value exists it will assign 0
                            values[a] = [self.q.get((k[0], a),0) for a in actionlist]
                            for a in actionlist:
                                values[a] = self.q.get((k[0], a),0)
                    for i in values:
                        if values[i] > 0:
                            #checking how many actions has a positive value if so the code will pick the best action out of                                 #those based on coutnvalues value.
                            countvalues = countvalues+1
                            #print countvalues
                    #If no postive values for action (assuming it has zero and negative values) the application will explore as                     #part of greedy search using random action as part of exploration and check the reward so that we can get                     #a positive value.(other wise it will pick 0 as max values if we have a negative values)
                    if countvalues < 1:
                        action = random.choice([None, 'forward', 'left', 'right'])
                        self.actionvalue = 1
                    else:
                        #if there are multiple positive values it will pick the action with maximum q value for that particular                         #state
                        action = max(values, key=values.get)
                        self.actionvalue = 1
                    #If the state is not present in Q table as it is a new state then application will take random action                           #as part of exploration
                    if self.actionvalue == 0:
                        action = random.choice([None, 'forward', 'left', 'right'])
                       
                #If the Q table is empty as it is a new state then application will take random action                                         #as part of exploration
                else:
                    action = random.choice([None, 'forward', 'left', 'right'])

                #Assigning key with previous state values (Assuming previousstae = currentstate) and nextstate as future state                 #in key1
                key = (self.previousstate,self.previousaction)
                key1 = (self.nextstate, action)
                
                #updating Q table for previous states
                self.q[key] = (1-self.alpha) * self.q.get(key, 0) + self.alpha * (self.reward+ self.gamma* self.q.get(key1, 0))


                #Assigning nextstate to previous state for future iterations.
                self.previousstate = self.nextstate
                self.previousaction = action 
                #Execute action and get reward for previousaction
                self.reward = self.env.act(self, self.previousaction)
                if self.reward < 0:
                    rewards.append(self.reward)
                else:
                    rewards.append(0)
                #print self.allrewards
                self.numberoftrails = self.numberoftrails+1
                deadlines = self.numberoftrails
                
       
            

        #print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    global alpha,gamma, numberoftrails, deadline1, destinationreached, allrewards, rewards, deadlines, alldeadlines
    destinationreached = []
    allrewards = []
    rewards = []
    alldeadlines = []
    alpha = 0.9
    gamma = 0.7
    numberoftrails = 0

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    #sim = Simulator(e, update_delay=3, display=True)
    sim = Simulator(e, update_delay=0.1, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False
    #print q
    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line
    
    
    #print "numberoftrails to reach destination in final trail run %d" %numberoftrails
    #print "deadline to reach destination in final trail run %d" %deadline1
    if numberoftrails > deadline1: 
            destinationvalue = 0
    else:
            destinationvalue = 1
            
    destinationreached.append(destinationvalue)
    allrewards.append(sum(rewards))
    alldeadlines.append(deadlines)
    
    print " aplha value for this run is %.2f and gamma value is %.2f" %(alpha,gamma)
    print destinationreached
    #print len(destinationreached)
    print "Total Negative rewards in all trails %d" %sum(allrewards)
    print "sum of negative rewards in last 10 trails %.2f" %sum(allrewards[-10:])
    print "Total steps in all trails %d" %sum(alldeadlines)
    print "sum of steps to reach in last 10 trails %d" %sum(alldeadlines[-10:])
    print "Reached destination in all trails %d" %sum(destinationreached)
    print "Reached destination in last 10 trails %d" %sum(destinationreached[-10:])

if __name__ == '__main__':
    run()
