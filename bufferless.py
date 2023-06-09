import random
#import matplotlib.pyplot as plt

# intensity (pr) of updates generated by device
lam = [0.3, 0.2, 0.1, 0.8]

# pr that transmission over link is successful
p = [0.5, 0.4, 0.6, 0.9]


#################################################################
#   Random Policy
#################################################################

def random_policy(lam, p):

    simlen = 0
    agesum = 0
    agesum_from_beginning = 0
    simlen_list = []  # list to store the simulation time at each time step
    agesum_list = []  # list to store the sum of ages at each time step
    warmup = 10000    # let the stochastic process run for a while
    K = [1, 1, 1, 1]  # age of devices

    
    while (simlen < 200000):
        
        if (simlen > warmup):
            agesum += sum(K)  # retain sum of device's ages
            
        # select RANDOM device K
        n = random.randint(0, len(K)-1) 
        
        # see whether a packet is sent
        update = random.uniform(0,1)  # pr(generate a packet)
        if (update < lam[n]):
            link = random.uniform(0,1)  # pr(send packet over link)
            if (link < p[n]): 
                K[n] = 0  # update succesful

        # add one to device's ages
        for m in range(0, len(K)):
            K[m] += 1

        simlen += 1  # move on next discrete time unit

        agesum_from_beginning += sum(K)
        agesum_list.append(agesum_from_beginning / simlen)
        simlen_list.append(simlen)
        
    return (agesum / (simlen - warmup))


#################################################################
#   Max Age Policy
#################################################################

def index_of_max_age(K):
    max_val = K[0]  # assume first element is the largest
    max_indices = [0]  # list of indices where max value occurs
    
    for i in range(1, len(K)):
        if K[i] > max_val:
            max_val = K[i]  # update max value if current value is larger
            max_indices = [i]  # reset max indices to current index
            
        elif K[i] == max_val:
            max_indices.append(i)  # add current index to max indices list
            
    # return some device with max age        
    return random.choice(max_indices)    
    

def max_age_policy(lam, p):
    simlen = 0
    agesum = 0
    agesum_from_beginning = 0
    simlen_list = []  # list to store the simulation time at each time step
    agesum_list = []  # list to store the sum of ages at each time step
    warmup = 10000    # let the stochastic process run for a while
    K = [1, 1, 1, 1]  # age of devices
    

    while (simlen < 200000):
        if (simlen > warmup):
            agesum += sum(K)  # retain sum of device's ages
            
        # select device with MAX age
        n = index_of_max_age(K)  # if K>1 devices have equal max, choose one randomly
        
        # see whether a packet is sent
        update = random.uniform(0,1)  # pr(generate a packet)
        if (update < lam[n]):
            link = random.uniform(0,1)  # pr(send packet over link)
            if (link < p[n]): 
                K[n] = 0  # update succesful
    
        # add one to device's ages
        for m in range(0, len(K)):
            K[m] += 1

        simlen += 1  # move on next discrete time unit
        
        agesum_from_beginning += sum(K)
        agesum_list.append(agesum_from_beginning / simlen)
        simlen_list.append(simlen)
            
    return (agesum / (simlen - warmup))


#################################################################
#   Whittle Index Policy
#################################################################

def whittle_index(a, lam, p):
    return (a + ((lam*p)/2)*(a*(a-1)))


def index_of_max_whittle(K, lam, p):
    max_val = whittle_index(K[0], lam[0], p[0])  # assume K[0] has largest Whittle index
    max_indices = [0]  # list of indices where max value occurs
            
    for i in range(1, len(K)):
        K_i = whittle_index(K[i], lam[i], p[i])
        
        if K_i > max_val:
            max_val = K_i  # update max value if current value is larger
            max_indices = [i]  # reset max indices to current index
            
        elif K_i == max_val:
            max_indices.append(i)  # add current index to max indices list
        
    return random.choice(max_indices)

    
def whittle_index_policy(lam, p):
    simlen = 0
    agesum = 0
    agesum_from_beginning = 0
    simlen_list = []  # list to store the simulation time at each time step
    agesum_list = []  # list to store the sum of ages at each time step
    warmup = 10000    # let the stochastic process run for a while
    K = [1, 1, 1, 1]  # age of devices
    

    while (simlen < 200000):
        if (simlen > warmup):
            agesum += sum(K)  # retain sum of device's ages
            
        # select device based on Whittle Index
        n = index_of_max_whittle(K, lam, p)
        
        # see whether a packet is sent
        update = random.uniform(0,1)  # pr(generate a packet)
        if (update < lam[n]):
            link = random.uniform(0,1)  # pr(send packet over link)
            if (link < p[n]): 
                K[n] = 0  # update succesful
    
        # add one to device's ages
        for m in range(0, len(K)):
            K[m] += 1

        simlen += 1  # move on next discrete time unit
        
        agesum_from_beginning += sum(K)
        agesum_list.append(agesum_from_beginning / simlen)
        simlen_list.append(simlen)
        
    return (agesum / (simlen - warmup))