# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    # Create an empty stack.
    #  Go through each token in the list.
    #  If the token is a number, convert it to an integer and push it onto the stack.
    #  If the token is an operator, pop the last two numbers from the stack.
    #  Perform the mathematical operation using those numbers.
    #  For division, truncate the result toward zero.
    #  Push the calculated result back onto the stack.
    #  Repeat until all tokens have been processed.
    #  Return the final number remaining in the stack 
    stack = []
    
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            stack.append(int(a / b))
        else:
            stack.append(int(token))
    
    return stack.pop()

print(eval_rpn(["2", "1", "+", "3", "*"]))
print(eval_rpn(["4", "13", "5", "/", "+"]))
        
        

            



def decode_string(s):
    # Outline:
    # Create an empty stack.
    # Create a variable to store the current text.
    # Create a variable to store the repeat count.
    # Go through each character in the encoded string.
    # If the character is a digit, build the repeat count.
    # If the character is [, save the current text and repeat count on the stack, then reset them.
    # If the character is ], retrieve the saved values and repeat the current text the required number of times.
    # If the character is a letter, add it to the current text.
    # After processing all characters, return the decoded text.
     stack = []
     current_text = ""
     repeat_count = 0
     for char in s:
         if char.isdigit() == True:
            repeat_count = repeat_count * 10 + int(char)
         elif char == "[":
             stack.append((current_text, repeat_count))
             current_text = ""
             repeat_count = 0
         elif char == "]":
            previous_text, saved_count = stack.pop()
            current_text = previous_text + current_text * saved_count
         else:
             current_text += char

     return current_text 

print(decode_string("3[a]2[bc]"))
            
            




def daily_temperatures(temps):
    
    # Outline:
    # Create an empty list called stack to store the positions of days waiting for a warmer temperature.
    #  Create a list called result containing a zero for every temperature in the input list.
    #  Use a for loop to go through each temperature by its index.
    #  While the stack is not empty, check whether the current temperature is warmer than the temperature at the position stored at the top of the stack.
    #  If the current temperature is warmer, remove the last stored position from the stack.
    #  Calculate how many days passed by subtracting that stored position from the current day's position.
    #  Store the calculated number of days in the result list at the position of the day that was waiting.
    #  Continue checking the stack because the current temperature might also be warmer than other previous days.
    #  After checking, add the current day's position to the stack.
    #  Continue until every temperature has been processed.
    #  Return the result list. Any positions that never found a warmer day will still contain zero.
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))



def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
