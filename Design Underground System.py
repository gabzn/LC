https://leetcode.com/problems/design-underground-system/
  
from collections import defaultdict

class UndergroundSystem:

    def __init__(self):                                  # key : value
        self.check_in_dict = defaultdict(tuple)          # id : (start station, start time)
        self.check_out_dict = defaultdict(list)          # (start station, end station) : [total time from start to end among all travllers, number of travellers]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_dict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.check_in_dict[id]
        del self.check_in_dict[id]
        
        total_time_spent_during_trip = t - check_in_time
        check_in_and_out_pair = (check_in_station, stationName)
        
        if len(self.check_out_dict[check_in_and_out_pair]) != 0:
            info = self.check_out_dict[check_in_and_out_pair]
            info[0] += total_time_spent_during_trip
            info[1] += 1
        else:
            self.check_out_dict[check_in_and_out_pair].append(total_time_spent_during_trip)
            self.check_out_dict[check_in_and_out_pair].append(1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        info = self.check_out_dict[(startStation, endStation)]
        return info[0] / info[1]
