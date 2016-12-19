# Description  
The code and process notebook is for Applied reinforcement learning to build a simulated vehicle navigation agent. 
# Objective  
The main object of the project is to model a complex control problem in terms of limited available inputs, and designing a scheme for smartcab to automatically learn an optimal driving strategy based on rewards and penalties.
.
# Getting Started  
For this project, you can find the smartcab folder containing the necessary project files on the Machine Learning projects GitHub, under the projects folder. This project contains three directories:

•	/logs/: This folder will contain all log files that are given from the simulation when specific prerequisites are met.  
•	/images/: This folder contains various images of cars to be used in the graphical user interface. You will not need to modify or create any files in this directory.  
•	/smartcab/: This folder contains the Python scripts that create the environment, graphical user interface, the simulation, and the agents. You will not need to modify or create any files in this directory except for agent.py.  
It also contains two files:  
•	smartcab.ipynb: This is the main file where you will answer questions and provide an analysis for your work. -visuals.py: This Python script provides supplementary visualizations for the analysis. Do not modify.  

Finally, in /smartcab/ are the following four files:  
•	## Modify:  
•	agent.py: This is the main Python file where you will be performing your work on the project.  
•	## Do not modify:  
•	environment.py: This Python file will create the smartcab environment.  
•	planner.py: This Python file creates a high-level planner for the agent to follow towards a set goal.  
•	simulator.py: This Python file creates the simulation and graphical user interface.  
# Running the Code
In a terminal or command window, navigate to the top-level project   directory smartcab/ (that contains the three project directories) and run one of the following commands:  
python smartcab/agent.py or  
python -m smartcab.agent  
This will run the agent.py file and execute your implemented agent code into the   environment. Additionally, use the command jupyter notebook smartcab.ipynb from this   same directory to open up a browser window or tab to work with your analysis notebook.   Alternatively, you can use the command jupyter notebook or ipython notebook and   navigate to the notebook file in the browser window that opens. Follow the instructions in   the notebook and answer each question presented to successfully complete the   implementation necessary for your agent.py agent file. A README file has also been   provided with the project files which may contain additional necessary information or   instruction for the project.    

# Files
The agent.py Python file with all code implemented as required in the instructed tasks.  
•	The /logs/ folder which should contain five log files that were produced from your simulation and used in the analysis.  
•	The smartcab.ipynb notebook file with all questions answered and all visualization cells executed and displaying results.  
•	An HTML export of the project notebook with the name report.html. 

# Official Data Description  
## Environment
The smartcab operates in an ideal, grid-like city (similar to New York City), with roads going in the North-South and East-West directions. Other vehicles will certainly be present on the road, but there will be no pedestrians to be concerned with. At each intersection there is a traffic light that either allows traffic in the North-South direction or the East-West direction. U.S. Right-of-Way rules apply:  
•	On a green light, a left turn is permitted if there is no oncoming traffic making a right turn or coming straight through the intersection.  
•	On a red light, a right turn is permitted if no oncoming traffic is approaching from your left through the intersection. To understand how to correctly yield to oncoming traffic when turning left, you may refer to this official drivers’ education video, or this passionate exposition.  
## Inputs and Outputs
Assume that the smartcab is assigned a route plan based on the passengers’ starting location and destination. The route is split at each intersection into waypoints, and you may assume that the smartcab, at any instant, is at some intersection in the world. Therefore, the next waypoint to the destination, assuming the destination has not already been reached, is one intersection away in one direction (North, South, East, or West). The smartcab has only an egocentric view of the intersection it is at: It can determine the state of the traffic light for its direction of movement, and whether there is a vehicle at the intersection for each of the oncoming directions. For each action, the smartcab may either idle at the intersection, or drive to the next intersection to the left, right, or ahead of it. Finally, each trip has a time to reach the destination which decreases for each action taken (the passengers want to get there quickly). If the allotted time becomes zero before reaching the destination, the trip has failed.  
## Rewards and Goal  
The smartcab will receive positive or negative rewards based on the action it as taken. Expectedly, the smartcab will receive a small positive reward when making a good action, and a varying amount of negative reward dependent on the severity of the traffic violation it would have committed. Based on the rewards and penalties the smartcab receives, the self-driving agent implementation should learn an optimal policy for driving on the city roads while obeying traffic rules, avoiding accidents, and reaching passengers’ destinations in the allotted time.  

