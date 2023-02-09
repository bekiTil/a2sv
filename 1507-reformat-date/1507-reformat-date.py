class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12", }
        date=[val for val in date.split(" ")]
        temp=[]
        val=date[0][:len(date[0])-2]
        if len(val)==1:
            val='0'+val
        temp.append(val)
        temp.append(month[date[1]])
        temp.append(date[2])
        print(temp)
        temp.reverse()
        return '-'.join(temp)