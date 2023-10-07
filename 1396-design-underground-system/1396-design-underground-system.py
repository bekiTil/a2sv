class UndergroundSystem:
    
    def __init__(self):
        
        self.checkedInDrivers={}
        
        self.stationsAverageTime= {}

    def checkIn(self, id:int, stationName:str,t:int) -> None:
        if id in self.checkedInDrivers:
            return 
        self.checkedInDrivers[id]=[stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedInDrivers:
            return 
        startStation , time = self.checkedInDrivers[id]
        
        timeTakenToTravel = t - time
        
        if (startStation,stationName) in self.stationsAverageTime:
            
            self.stationsAverageTime[(startStation,stationName)][0] += timeTakenToTravel
            self.stationsAverageTime[(startStation,stationName)][1] += 1
        else:
            self.stationsAverageTime[(startStation,stationName)] = [timeTakenToTravel, 1]
        
        self.checkedInDrivers.pop(id)
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stationsAverageTime[(startStation,endStation)][0]/self.stationsAverageTime[(startStation,endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)