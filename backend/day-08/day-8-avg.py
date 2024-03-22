my_list = [5, 9, 2, 3, 1]

sum = 0
avg = 0

for num in my_list:
    sum += num

avg = sum / len(my_list)
print(avg)

# DEBUGGER NOTES:
#(1). Breakpoints(red circle), used along the side/gutter of the
#(2). number lines of code in order to check what is happening within
#(3). that placed breakpoint. Can place as many as you want if necessary.
#3 Tools in a Debugger: 
#(4). STEP OVER - moves into the next line of code.
#(5). STEP INTO - steps into methods,functions, or anything that is happening
#                 on the current line.
#(6). STEP OUT - takes us out the current scope, we go right back at the last statement 
#                or whatever function we're into. 