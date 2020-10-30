
def largestProduct():
    gridTXT  = open("EulerProblems/T1/11.20*20Grid.txt", "r") 
    lines = gridTXT.readlines()
    matrix = []

    #convert grid in matrix
    for lineCount in range(0, len(lines)):
        matrix.append([])
        for rowCount in range(0, len(lines[lineCount]),3):
            matrix[lineCount].append(int(lines[lineCount][rowCount:rowCount+2]))
    
    result = 0
    for lineCount in range(0,len(matrix)):
        for rowCount in range(0,len(matrix[lineCount])):
            #Check Down
            if (lineCount < len(matrix)-3):
                test = matrix[lineCount][rowCount] * matrix[lineCount+1][rowCount] * matrix[lineCount+2][rowCount] * matrix[lineCount+3][rowCount]
                if (test > result):
                    result=test
                    
            #Check Right
            if (rowCount < len(matrix[lineCount])-3):
                test = matrix[lineCount][rowCount] * matrix[lineCount][rowCount+1] * matrix[lineCount][rowCount+2] * matrix[lineCount][rowCount+3]
                if (test > result):
                    result=test
                
            #Check Diagonally (right/down)
            if ((rowCount < len(matrix)-3)) and (lineCount < len(matrix[lineCount])-3):  
                test = matrix[lineCount][rowCount] * matrix[lineCount+1][rowCount+1] * matrix[lineCount+2][rowCount+2] * matrix[lineCount+3][rowCount+3]
                if (test > result):
                    result=test
            
            #Check Diagonally (right/up)
            if ((rowCount < len(matrix)-3) and (lineCount > 3)):  
                test = matrix[lineCount][rowCount] * matrix[lineCount-1][rowCount+1] * matrix[lineCount-2][rowCount+2] * matrix[lineCount-3][rowCount+3]
                if (test > result):
                    result=test
    return result

print(largestProduct())