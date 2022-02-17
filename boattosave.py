class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        number_of_boat=0
        first=0
        last=len(people)-1
        while first<=last:
            if first==last:
                number_of_boat+=1
                break
            else:
                if people[last]+people[first]<=limit:
                    number_of_boat+=1
                    last-=1
                    first+=1
                else:
                    number_of_boat+=1
                    last-=1
        return number_of_boat
