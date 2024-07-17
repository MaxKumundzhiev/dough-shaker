"""
https://leetcode.com/problems/insert-interval/

Given a list of non-overlapping intervals sorted by their startTime, 
insert a given interval at the correct position and merge all necessary intervals 
to produce a list that has only mutually exclusive intervals.
"""


def insert(intervals, new_interval):
    merged = []
    i = 0

    # Add intervals before the new interval (no overlap)
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1

    # Start interval to be merged or replaced
    start = new_interval[0]
    end = new_interval[1]

    # Merge or replace overlapping intervals
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    # Add the merged or new interval
    merged.append([start, end])

    # Add remaining non-overlapping intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged