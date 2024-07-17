"""
https://leetcode.com/problems/merge-intervals/

Given a list of intervals, merge all the overlapping intervals 
to produce a list that has only mutually exclusive intervals.
"""


# Time O(N * logN) | Space O(M)
def merge_intervals(intervals):
    """
    - Traverse intervals until reach such an interval which does not overlap
    - Once reach un overlapping intervals, merge all previous intervals
        - update current start and current end
    """

    if len(intervals) < 2:
        return intervals  # No merging needed for less than 2 intervals

    # Sort intervals by start time for efficient merging
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        # Check for overlap
        if start <= current_end:
            # Merge overlapping intervals
            current_end = max(current_end, end)
        else:
            # No overlap, add current interval to merged list and update
            merged_intervals.append([current_start, current_end])
            current_start, current_end = start, end

    # Add the last interval if not already merged
    merged_intervals.append([current_start, current_end])

    return merged_intervals



assert merge_intervals([[1, 4], [2, 5], [7, 9]]) == [[1, 5], [7, 9]]