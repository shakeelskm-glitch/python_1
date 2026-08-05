'''#1.program to print numbers from 1 to n using recursion
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)
print_numbers(10)

#2.program to print numbers from n to 1 using recursion
def reverse(n):
    if n > 0:
        print(n)
        reverse(n - 1)  
reverse(10)
''
#3.program to find the sum of first n natural numbers using recursion
def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)
print("Sum of first natural numbers is:", sum(0))
''
#4.program to find the factorial of a number using recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))''

#5.program to generate fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(int(input("Enter the number of terms: "))))
''
#6.program to calculate the power of a number using recursion
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
x=int(input("Enter the base: "))
n=int(input("Enter the exponent: "))
print("Result:", power(x,n))
''

#7.program to count the number of digits in a number using recursion
def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)
n = int(input("Enter a number: "))
if n == 0:
    print("Number of digits in the number is: 1")
else:
    print("Number of digits in the number is:", count_digits(n))
''

#8.program to find sum of digits in a number using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
n = int(input("Enter a number: "))
print("Sum of digits in the number is:", sum_of_digits(abs(n)))
'''''
'''
#9. program to reverse a number using recursion
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)
n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))''

#10.program to check whether a string is a palindrome or not using recursion
def palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return palindrome(text[1:-1])
text = input("Enter a string: ")
if palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")''

#11.program to find GCD of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD of", a, "and", b, "is:", gcd(a, b))''

#12.program to find LCM of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
lcm = (a * b) // gcd(a, b)
print("LCM of", a, "and", b, "is:", lcm)
''


#13.program to find binary search using recursion
def binary_search(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return -1
arr=list(map(int,input("Enter elements:").split()))
key=int(input("Enter the key: "))
result = binary_search(arr, 0, len(arr) - 1, key)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
    ''

#14.program to generate all posible subsets of a given list using recursion
def generate_subsets(arr, index=0, current=[]):
    if index == len(arr):
        print(current)
        return
    generate_subsets(arr, index + 1, current)
    generate_subsets(arr, index + 1, current + [arr[index]])
arr=list(map(int,input("Enter elements:").split()))
generate_subsets(arr)
''

#15.program to generate all possible permutations of a given string using recursion
def permutations(s,answer):
    if len(s)==0:
        print(answer,end=" ")
        return
    for i in range(len(s)):
        ch=s[i]
        left_substr=s[0:i]
        right_substr=s[i+1:]
        rest=left_substr+right_substr
        permutations(rest,answer+ch)

s = input("Enter a string: ")
permutations(s, "")

''

#16.program to generate all combinations of balanced parentheses using recursion
def parentheses(n, open_count=0, close_count=0, current=""):
    if len(current) == 2 * n:
        print(current)
        return
    if open_count < n:
        parentheses(n, open_count + 1, close_count, current + "(")
    if close_count < open_count:
        parentheses(n, open_count, close_count + 1, current + ")")
n=int(input("Enter the number of pairs of parentheses: "))
parentheses(n)''

#17.program to solve the N-Queens problem using recursion
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True
def print_board(board,n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
def solve_n_queens_util(board, row, n):
    if row == n:
        print_board(board, n)
        return
    for col in range(n):
        if is_safe(board, row,col, n):
            board[row]=col
            solve_n_queens_util(board, row + 1, n)
            board[row] = -1  
def solve_n_queens(n):
    board = [-1] * n
    solve_n_queens_util(board, 0, n)
n=int(input("Enter the number of queens: "))
solve_n_queens(n)''

#18.Rat in maze problem using recursion
def solve_maze(maze, x, y, n, sol):
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 1:
        sol[x][y] = 1
        if solve_maze(maze, x + 1, y, n, sol):
            return True
        if solve_maze(maze, x, y + 1, n, sol):
            return True
        sol[x][y] = 0
        return False
    return False
n = int(input("Enter the size of the maze: "))
print("Enter the maze (1 for path, 0 for blocked):")
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)
sol = [[0] * n for _ in range(n)]
if solve_maze(maze, 0, 0, n, sol):
    print("Path found:")
    for row in sol:
        print(*row)
else:
    print("No path found.")
    '''

#19. sudoku solver using recursion
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True
number = 0
def solve_sudoku(board):
    global number
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    number += 1
    print(f"Solution {number}:")
    for r in board:
        print(r)
    return True
n = 9
board = [[0] * n for _ in range(n)]
print("Enter the Sudoku puzzle (0 for empty cells):")
for i in range(n):
    row = list(map(int, input().split()))
    board[i] = row
solve_sudoku(board)