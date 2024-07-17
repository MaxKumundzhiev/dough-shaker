"""
Given a set of intervals, find out if any two intervals overlap.

Intervals: [[1,4], [3,5], [3,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap
"""


def find_overlapping_intervals(intervals) -> bool:
    intervals.sort(key = lambda interval: interval[0])

    for idx in range(1, len(intervals)):
        current_start, current_end = intervals[idx]
        previous_start, previous_end = intervals[idx-1]
        
        if current_start <= previous_end:
            return True
    
    return False
