class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        degree={}
        memo={}
        for i in range(len(recipes)):
            degree[recipes[i]]=len(ingredients[i])
            for j in ingredients[i]:
                if j in degree:
                    pass
                else:
                    degree[j]=0
                if j in memo:
                    memo[j].append(recipes[i])
                else:
                    memo[j]=[recipes[i]]
        level=deque([])
        
        for i in degree:
            if degree[i]==0:
                level.append(i)
        ans=[]
       
        while level:
            food=level.popleft()
           
            if food in recipes:
                ans.append(food)
                supplies.append(food)
            if food not in memo:
                continue
            for i in memo[food]:
                if food in supplies:
                    degree[i]-=1
                    if degree[i]==0:
                        level.append(i)
        
        return ans
