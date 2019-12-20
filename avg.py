'''
About:
This program generates N random number which is between min-max value
and the total average is avg
Note: all numbers with 2 Decimal precision
------------------------------------------------------------------------
Author: Shahim Vedaei
Last modification: Dec 19 2019
'''
#-- Libraries import
import numpy as np
import random
#===================== BEGIN
#-- INPUTS
avg = 4950.70
min = 4877
max = 5220.23
N   = 14
#------------------------------
#-- Processing
arr = 0;
for i in range(N-2): #--- 2 spots are reserved for MIN/MAX
    arr = np.around( np.append(arr, random.uniform(min-avg, max-avg)), decimals=2)

arr=np.delete(arr,0) #-- remove first 0 element

diff=sum(arr) + (min-avg) + (max-avg) #--- Howmuch random numbers is deviated from average
diff_Float = np.around(diff-int(diff), decimals=2);
diff_Integer = int(diff);

arr = arr-np.around(diff_Integer/len(arr),decimals=2) #--- Make average to zero
arr[-1] = arr[-1]-diff_Float;

arr = arr + avg; #--- Trasfer to avg value
arr = np.append(arr, min) #--- append MIN
arr = np.append(arr, max) #--- append MAX
np.random.shuffle(arr) #--- shuffle all data to randomly placed the indexes

#-- Print outputs
print("AVERAGE= " + str(np.average(arr)))
print(np.reshape(arr,(N,1)))
#===================== END
