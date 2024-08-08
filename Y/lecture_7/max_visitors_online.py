"""
Сайт посетило N человек. Для каждого известно время входа на сайт i-th и выхода o-th. 
Считается, что человек был на сайте с момента i-th по o-th включетельно. 

Определите какое максимальное кол-во человек было на сайте одновременно.
"""

from typing import List
from datetime import datetime


def max_visitors_online(
    visitors: int, time_in: List[datetime], time_out: List[datetime]
) -> int:
    
    type_in, type_out =  -1, 1
    events = []

    for idx in range(visitors):
        events.append((time_in[idx], type_in))
        events.append((time_out[idx], type_out))
    events.sort()

    online, max_online = 0, 0
    for event in events:
        if event[1] == type_in:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)

    return max_online


visitors = 10
start_times = ["07:30", "12:00", "15:30", "09:00", "11:15", "14:00", "16:45", "08:15", "10:30", "13:45"]
end_times = ["09:15", "13:45", "17:15", "10:30", "12:45", "15:30", "18:15", "09:45", "12:00", "15:15"]

max_visitors_online(
    visitors=visitors, time_in=start_times, time_out=end_times
)