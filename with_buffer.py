import random
#import matplotlib.pyplot as plt

#################################################################
#   Random Policy
#################################################################
def random_policy(lam, p):
    a = 0 # time since last update in the device; AoI seen by device
    d = 0 # AoI, seen by monitor (base station)
    agesum = 0
    iternum  = 0
    initrun = 10000
    DEVICE_AGES = [(0, 1), (0, 1), (0, 1), (0, 1)] # (a, d) parameters for each device
    
    
    # simulation loop, number of iterations = 200 000.
    while (iternum  < 200000):
        # choose a device, generate pr for successful update and transmission over link
        n = random.randint(0, len(DEVICE_AGES)-1) 
        update = random.uniform(0,1)
        link = random.uniform(0,1) 
      
        # let simulation run for initrun units before collecting age data
        if (iternum  > initrun):
            agesum += sum(map(sum, DEVICE_AGES))
        
        # For scheduled device: 4 cases
        # Age parameters of scheduled device 
        a, d = DEVICE_AGES[n]
    
        # case 1: all updates and transmissions are successful
        # case 3: update is successful but transmission is not
        if (update < lam[n]):
            if (link < p[n]):   
                a = 0
                d = 1
            else:   
                d = a + d + 1
                a = 0
                
        # case 2: update is unsuccessful but transmission is successful
        # case 4: neither update nor transmission is successful
        else:
            if (link < p[n]):
                d = 1
                a += 1
            else:
                a += 1

        # assign TWO AGE PARAMETERS to selected device
        DEVICE_AGES[n] = (a, d)

        # for devices that were not selected
        for m in range(0, len(DEVICE_AGES)):
            if (m != n):   
                a, d = DEVICE_AGES[m]
                
                # case 1: the device has generated an update
                if (update < lam[m]):
                    d = a + d + 1
                    a = 0
        
                # case 2: the device has not generated an update
                else:   
                    a += 1
                    
                # assign age to the device
                DEVICE_AGES[m] = (a, d)

        # calculate average age for each K
        iternum += 1
        
    # return average Age-of-Information for the scheduling policy
    return (agesum / (iternum - initrun))

#################################################################
#   Max Age Policy
#################################################################

def index_of_max_age(DEVICE_AGES):
    age_total = [sum(device) for device in DEVICE_AGES]  # Calculate the total age of each device
    max_val = age_total[0]  # Assume the first element is the largest
    max_indices = [0]  # Initialize the list of indices where the maximum value occurs
    
    # Iterate over the age_total list starting from the second element
    for i in range(1, len(age_total)):
        if age_total[i] > max_val:
            max_val = age_total[i]  # Update the maximum value if the current value is larger
            max_indices = [i]  # Reset the list of maximum indices to the current index
        elif age_total[i] == max_val:
            max_indices.append(i)  # Add the current index to the list of maximum indices
        
    
    # Return the index of a device with the maximum age. 
    return random.choice(max_indices)  # If >1 devices with same age, select arbitrarily.


def max_age_policy(lam, p):
    a = 0  # time since last update in the device; AoI seen by device
    d = 0  # AoI, seen by monitor (base station)
    agesum = 0  # sum of ages of all devices
    iternum = 0  # current simulation time
    initrun = 10000  # initialization run length
    DEVICE_AGES = [(0, 1), (0, 1), (0, 1), (0, 1)]  # list of devices
    
    while (iternum < 200000):
        # select device and generate random values
        n = index_of_max_age(DEVICE_AGES)  # index of device with the maximum age
        update = random.uniform(0,1)  # random number for update
        link = random.uniform(0,1)  # random number for transmission link
        
        if (iternum > initrun):
            # average age: (a + d) for each K
            agesum += sum(map(sum, DEVICE_AGES))  # sum of ages of all devices
            
        # selected device's parameters
        a, d = DEVICE_AGES[n]
        
        if (update < lam[n]):  # update successful
            if (link < p[n]):  # case 1: update and transmission both successful
                a = 0
                d = 1
                
            else:  # case 3: update successful, but transmission failed
                d = a + d + 1
                a = 0
                
                
        else:  # update failed
            if (link < p[n]):  # case 2: update failed, but transmission successful
                d = 1
                a += 1
                
            else:  # case 4: both update and transmission failed
                a += 1

        # update selected device's age
        DEVICE_AGES[n] = (a, d)
        

        # for devices not selected: 2 cases
        for m in range(0, len(DEVICE_AGES)):
            if (m != n):  # if device (m) is not the selected device (n)
                a, d = DEVICE_AGES[m]
                
                if (update < lam[m]):  # case 1: device generated update
                    d = a + d + 1
                    a = 0
        
                else:  # case 2: device did not generate update
                    a += 1
                    
                # update the age of the device
                DEVICE_AGES[m] = (a, d)
                
        iternum += 1
        # while-loop ends

    # return average Age-of-Information for the scheduling policy
    return (agesum / (iternum - initrun))

#################################################################
#   Whittle Index Policy
#################################################################

def whittle_index(a, lam, p):
    return (a + ((lam*p)/2)*(a*(a-1)))


def index_of_max_whittle(DEVICE_AGES, lam, p):
    ages_total = [sum(device) for device in DEVICE_AGES]
    max_val = whittle_index(ages_total[0], lam[0], p[0])  # assume K[0] has largest Whittle index
    max_indices = [0]  # list of indices where max value occurs
            
    for i in range(1, len(ages_total)):
        DEVICE_AGES_i = whittle_index(ages_total[i], lam[i], p[i])
        
        if DEVICE_AGES_i > max_val:
            max_val = DEVICE_AGES_i  # update max value if current value is larger
            max_indices = [i]  # reset max indices to current index
            
        elif DEVICE_AGES_i == max_val:
            max_indices.append(i)  # add current index to max indices list
        
    return random.choice(max_indices)


def whittle_index_policy(lam, p):
    a = 0
    d = 0
    agesum = 0
    iternum = 0
    initrun = 10000
    DEVICE_AGES = [(0, 1), (0, 1), (0, 1), (0, 1)]   # (a, d)

    while (iternum < 200000):
        # choose a device, generate random numbers
        n = index_of_max_whittle(DEVICE_AGES, lam, p) 
        update = random.uniform(0,1)
        link = random.uniform(0,1) 
        
        
        if (iternum > initrun):
            agesum += sum(map(sum, DEVICE_AGES))
        
    
        # parameters of the scheduled device
        a, d = DEVICE_AGES[n]
  
        if (update < lam[n]):   # update succeeded
            if (link < p[n]):   # case 1: both update and transmission succeeded
                a = 0
                d = 1
                
            else:   # case 3: update succeeded, but transmission failed
                d = a + d + 1
                a = 0
                
        else:   # update failed
            if (link < p[n]):    # case 2: update failed, but transmission succeeded
                d = 1
                a += 1
                
            else:   # case 4: both update and transmission failed
                a += 1
                
        # assign age to the device
        DEVICE_AGES[n] = (a, d)
        
        # non-scheduled devices: 2 cases
        for m in range(0, len(DEVICE_AGES)):
            if (m != n):   # if device (m) is not the scheduled device (n)
                a, d = DEVICE_AGES[m]
                
                if (update < lam[m]):   # case 1: device generated an update
                    d = a + d + 1
                    a = 0
        
                else:   # case 2: device did not generate an update
                    a += 1
                    
                # assign age to the device
                DEVICE_AGES[m] = (a, d)
                
        iternum += 1
        # end of while loop
        
    # return average Age-of-Information for the scheduling policy
    return (agesum / (iternum - initrun))
