"""
Сайт посетило N человек. Для каждого известно время входа на сайт i-th и выхода o-th. 
Считается, что человек был на сайте с момента i-th по o-th включетельно. 

Определите какое суммарное время на сайте был хотя бы один человек.

Если мы пришли в событие с положительным счетчиком количнства людей, 
то между этим и предыдущим событием  на сайте кто то был. Прибавим к ответу  
"""

def time_with_vistors(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i]), -1)
        events.append((tout[i]), 1)
    events.sort()

    online = 0
    not_empty_time = 0

    for i in range(len(events)):
        if online > 0:
            not_empty_time += events[i][0] - events[i-1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1

    return not_empty_time
        