import heapq as hq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        new={}
        frequent=[]
        for i in words:
            if i in new:
                new[i]+=1
            else:
                new[i]=1
        print(new)
        news=[]
        for i,y in new.items():
            news.append((-1*y,i))
        print(news)
        hq.heapify(news)
        n=0
        while n<k:
            
            frequent.append(hq.heappop(news)[1])
            n+=1
        
        return frequent
        
        
