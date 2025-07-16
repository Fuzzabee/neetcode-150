### INSTRUCTIONS ###
# Given an array of meeting time interval objects consisting of start and end times
# [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their
# schedule without any conflicts.
#
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
#
# Input: intervals = [(5,8),(9,15)]
# Output: true
####################

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def canAttendMeetings(intervals):
    busyTimes = set()
    for interval in intervals:
        beginTime = interval.start
        endTime = interval.end
        for i in range(beginTime, endTime + 1):
            prevLen = len(busyTimes)
            busyTimes.add(i)
            if prevLen == len(busyTimes) and i != beginTime and i != endTime: return False

    return True

def main():
    m1 = Interval(0,30)
    m2 = Interval(5, 10)
    m3 = Interval(15, 20)
    print(canAttendMeetings([m1, m2, m3]))

    m1 = Interval(5, 8)
    m2 = Interval(9, 15)
    print(canAttendMeetings([m1, m2]))

if __name__ == "__main__":
    main()