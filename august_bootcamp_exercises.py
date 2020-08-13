
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

###########

input('Press enter to start')
start_time = time.time()
print('Starting stopwatch at ', time.strftime(
    '%I:%M:%S %p')) # %I as 12hr clock, %p as AM/PM addition

input('Press enter to stop')
end_time = time.time()
time_elapsed = round(end_time - start_time, 2)
print('Time elapsed: ', time_elapsed, ' seconds.')

################
# Check if input is text
while True:
    q3 = input('Pease input a word: ')
    if q3.isalpha():
        print('Thank you!')
        break
    else:
        print('Please try again...')