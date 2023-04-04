# Scheduling Policy Performance Analysis
Scheduling policies performance analysis using mean Age-of-Information (AoI) as the unit of measurement. 

The analysis is done using this simulation of network with 4 devices.


Run the program from main.py file. 

Results are displayed in the console. 


The work on the simulation is still in progress.
This simulation is part of a bachelor thesis' and its being developed by Rami Ghoniem, 2023.


# System Model
A scheduling policy is used to determine, how base station desides to select a device in the network to check for an update. 

There are 4 devices in the system, that generate updates randomly. 

Each device has its own intensity parameter, lam, that determines intensity of generating new update. 
There is also random success parameter to determine probability of successful transmission over a link to the base station.


# Read More
One can read about Age-of-Information from R. D. Yates, Y. Sun, D. R. Brown, S. K. Kaul, E. Modiano and S. Ulukus, "Age of Information: An Introduction and Survey," in IEEE Journal on Selected Areas in Communications, vol. 39, no. 5, pp. 1183-1210, May 2021, doi: 10.1109/JSAC.2021.3065072.

System model is motivated by P. Lassila and S. Aalto, "Near-optimal uplink scheduling for age-energy tradeoff in wireless systems," 2021 33th International Teletraffic Congress (ITC-33), Avignon, France, 2021, pp. 1-9.


