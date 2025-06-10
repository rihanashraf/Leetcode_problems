class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        i = 0
         
        # for rows
        while i < 9:
            dicti = {}
            for number in board[i]:
                if number in dicti:
                    return False
                elif number != ".":
                    dicti[number] = 1
            i +=1
        
        #for columns
        for i in range(9):
            dicti = {}
            for j in range(9):
                item = board[j][i]
                if item in dicti:
                    return False
                elif item != ".":
                    dicti[item] =1

        # WHy doesn't the while loop work???
        # works till now i think, need to create something for the 3*3 subs

        # for 3*3 subs
        starts = [(0, 0) , (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]
        
        for i, j in starts:
            s= set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)
                
        return True
                
        #In this particular case,
        # Time : O(1)
        # Space : O(1)
        #because it is a finite set of 9*9 and doesnt take time

        #If it were a very large set, then
        # Time : O(n^2) because you're looking at all the elements in the set multiple times
        # 2 for loops
        #Space : O(n) because storing in dicti for everytime in n for row, column or 3*3 grid, all are n so sum of muliple n's or like O(3n) boiled down to O(n)        