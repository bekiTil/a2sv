import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        value={}
        new=[]
        app=[]
        for i in range(len(points)):
            news=0
            for j in range(len(points[i])):
                news+=(points[i][j])**2
            value[i]=(math.sqrt(news))
        print(value)
        value=dict(sorted(value.items(), key=lambda x: x[1]))
        print(value)
        i=0
        for key in value.keys():
            if i<k: 
                print(key)
                app.append(points[key])
            i+=1
        return app
