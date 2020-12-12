class Solution(object):
    def print_matrix_in_spiral_order(self, matrix):
        spiral_order_list_from_matrix = []
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        size = len(matrix) * len(matrix[0])

        print("Top:" +str(top))
        print("Bottom:" +str(bottom))
        print("Left:" +str(left))
        print("Right:" +str(right))
        print("Size:" +str(size))

        while len(spiral_order_list_from_matrix) < size:

            for i in range(left, right+1):
                spiral_order_list_from_matrix.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                spiral_order_list_from_matrix.append(matrix[i][right])
            right -= 1

            for i in range(right, left-1, -1):
                spiral_order_list_from_matrix.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top-1, -1):
                spiral_order_list_from_matrix.append(matrix[i][left])
            left += 1

        return spiral_order_list_from_matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
print(Solution().print_matrix_in_spiral_order(matrix))
