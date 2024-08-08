"""
Сайт посетило N человек. Для каждого известно время входа на сайт i-th и выхода o-th. 
Считается, что человек был на сайте с момента i-th по o-th включетельно. 
Начальник заходил на сайт M раз в моменты времени Boss и смотрел сколько людей сейчас на сайте.
Посещения сайта начальником упорядочены по возрастанию. 

Определите, какие показания счетчика людей увидел начальник.

Решение
    Добавим 3 тип ивента - "начальник зашел на сайт" и при наступлении такого события, 
    будем сохранять счетчик
"""

"""
1   2   1   2  1   2  1       0
|-------|
    |----------|   |----------|
            |---------|
"""


def online_counter(
    visitors, time_in, time_out, bosses, boss_in
):
    
    events = []
    user_log_in_type, user_log_out_type, boss_log_in_type = 1, -1, 0


    for idx in range(len(visitors)):
        user_in_time, user_out_time, boss_in_time = time_in[idx], time_out[idx], boss_in[idx]
        events.append((user_in_time, user_log_in_type))
        events.append((user_out_time, user_log_out_type))
        events.append((boss_in_time, boss_log_in_type))
    
    events.sort()

    online = 0
    answer = []

    for event in events:
        event_type = event[1]
        # order of if-s might be dependent of the problem conditions
        # example: if all 3 events occurred at the same time
        """
               *
        |------|
               |------|
        """

        if event_type == user_log_in_type:
            online += 1
        elif event_type == user_log_out_type:
            online -= 1
        else:
            answer.append(online)
    
    return answer
    

