class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ticket = tickets[k]
        result = 0
        for i in range(len(tickets)):
            if tickets[i] <= ticket and tickets[i] > 0 :
                result += tickets[i]
            if tickets[i] > ticket and tickets[i] > 0:
                result += ticket
            if i>k and tickets[i] >= ticket:
                result -= 1
           
        return result
        