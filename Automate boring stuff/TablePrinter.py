#! python3
# printTable.py - takes a list of lists of strings and presents it in a 
# well-organized table.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable():
    colWidths=[0]*len(tableData)
    for list in range(len(tableData)):
        for item in range(len(tableData[list])):
            if colWidths[list]<len(tableData[list][item]):
                colWidths[list]=len(tableData[list][item])                
    for item in range(len(tableData[list])):
        print(tableData[0][item].rjust(colWidths[0]+2) + tableData[1][item].rjust(colWidths[1]+2) + tableData[2][item].rjust(colWidths[2]+2))

printTable()
