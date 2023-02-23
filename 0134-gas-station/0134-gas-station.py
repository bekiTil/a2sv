class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       
            net =0

            index = 0

            total = 0

            for i in range(len(gas)):
                total+= (gas[i]- cost[i])

            if total<0:
                return -1

            for i in range(len(gas)):
                # checking the running sum 
                net += gas[i]- cost[i]
                if net<0:
                    index = i +1
                    net =0

            if index == len(gas):
                return -1

            return index
