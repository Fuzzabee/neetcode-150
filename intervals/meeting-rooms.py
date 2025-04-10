# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
# determine if a person could add all meetings to their schedule without any conflicts.

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import collections

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
     

def canAttendMeetings(intervals):
    # Dictionary to store start/end times, will sort by start time for check
    orderedIntervals = {}
    for interval in intervals:
        if interval.start in orderedIntervals:
            return False
        orderedIntervals[interval.start] = interval.end
    
    orderedIntervals = collections.OrderedDict(sorted(orderedIntervals.items()))

    keys = list(orderedIntervals.keys())
    keys.sort()

    for key1, key2 in zip(keys, keys[1:]):
        if orderedIntervals.get(key1) > key2:
            return False

    return True


def main():
    # Input: intervals = [(0,30),(5,10),(15,20)]
    # Output: false
    i1 = Interval(0, 30)
    i2 = Interval(5, 10)
    i3 = Interval(15, 20)
    print(canAttendMeetings([i2, i1, i3]))

    # Input: intervals = [(5,8),(9,15)]
    # Output: true
    i1 = Interval(5, 8)
    i2 = Interval(9, 15)
    print(canAttendMeetings([i1, i2]))

if __name__ == "__main__":
    main()