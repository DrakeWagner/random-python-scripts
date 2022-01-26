# angle between the hour and minute hands of a clock

def clock_angle(hour, minute):
    hour_in_minutes = (hour * 5) + ((1 / minute) * 60)
    floating_degree_hour = hour_in_minutes * 6
    floating_degree_minutes = minute * 6

    degree_difference = floating_degree_hour - floating_degree_minutes

    print(degree_difference)

clock_angle(6, 30)
clock_angle(10, 45)

