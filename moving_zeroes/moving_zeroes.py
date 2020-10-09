'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    
    left = []
    right = []
    
    for num in arr:
        if num == 0:
            right.append(num)
            
            print(left, "left", right, "right")
        else:
            left.append(num)
            
            print(left, "left", right, "right")
            
    return left + right


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")