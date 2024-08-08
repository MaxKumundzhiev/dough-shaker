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
