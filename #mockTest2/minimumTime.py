time = [1,2,3]
totalTrips = 5
def minimumTime(time, totalTrips):

        minTime = 1
        totalTripCnt = 0
        i = 0
        tripCnts = [0]*len(time)
        while totalTripCnt < totalTrips:
          tripCnts[i] = time[i]//minTime
          i += 1

          if i == len(time)-1:
            totalTripCnt = sum(tripCnts)
            i = 0
            minTime += 1
        return totalTripCnt

print(minimumTime(time, totalTrips))
