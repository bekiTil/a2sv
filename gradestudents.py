def gradingStudents(grades):
    # Write your code here
    new=[]
    for grade in grades:
        if grade<35:
            new.append(grade)
        elif (grade%5)>=3:
            
            if (grade%5)%2==0:
                new.append(grade + 1)
            else:
                new.append(grade + 2)
        else:
           
            new.append(grade)
    return new
