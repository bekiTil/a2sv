class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row=len(image)
        column=len(image[0])
        upcoming=[(sr,sc)]
        number=image[sr][sc]
        vistied=[]
        while upcoming:
            x,y=upcoming.pop()
            vistied.append((x,y))
            image[sr][sc]=newColor
            
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=i<row and 0<=j<column and number==image[i][j] and (i,j) not in vistied:
                    image[i][j]=newColor
                    upcoming.append((i,j))
        return image
                    
