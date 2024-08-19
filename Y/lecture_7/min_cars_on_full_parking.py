
def min_cars_on_full_parking(cars, n):
    """Function, which counts minimal cars on full parking."""

    events = []

    for idx, car in enumerate(cars):
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1, idx))
        events.append((timeout, -1, placeto - placefrom + 1, idx))
    
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1

    for idx, event in enumerate(events):
        if event[1] == -1:
            occupied -= event[2]
            nowcars -= 1
        elif event[1] == 1:
            occupied += event[2]
            nowcars += 1
        if occupied == n and nowcars < mincars:
            mincars = nowcars

    carnums = set()
    nowcars = 0
    for idx, event in enumerate(events):
        if event[1] == -1:
            occupied -= event[2]
            nowcars -= 1
            carnums.remove(event[3])
        elif event[1] == 1:
            occupied += event[2]
            nowcars += 1
            carnums.add(event[3])
        if occupied == n and nowcars == mincars:
            return carnums
    return set()
