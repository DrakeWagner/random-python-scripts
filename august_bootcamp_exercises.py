
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


input('Press enter to start')
start_time = time.time()
print('Starting stopwatch at ', start_time)

input('Press enter to stop')
end_time = time.time()
time_elapsed = round(end_time - start_time, 2)
print('Time elapsed: ', time_elapsed, ' seconds.')

################

