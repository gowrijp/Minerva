#https://towardsdatascience.com/many-python-programmers-cannot-solve-this-puzzle-c5950841d14d
import time

start_time = time.time()

for i in range(10**7):
    x = i%5
    
finish_time = time.time()
print("Duration: {} msec".format((finish_time-start_time)*1000))

# Duration: 960.4330062866211 msec

#------------------------------------------------------------------------------------

def main():
    for i in range(10**7):
        x = i % 5

start_time = time.time()
main()
finish_time = time.time()

print("Duration: {} msec".format((finish_time-start_time)*1000))

# Duration: 408.9057445526123 msec
