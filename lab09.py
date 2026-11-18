# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    #  loop through the array using nested for loops, search for the two numbers that will add of to target by testing every instance of the loop, create addition sentence
   
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums [j] ==target:
                return[i,j]


def max_profit(prices):
    #   loop through the array to find the lowest number, if not found return 0, if found search for the biggest number after the smallest index, once found return biggest take away smallest
   if not prices:
        return 0

   lowest = prices[0]
   best_profit = 0
   
   for price in prices:
        if price < lowest:
            lowest = price
        elif price - lowest > best_profit:
            best_profit = price - lowest
   return best_profit

def max_subarray(nums):
    #   loop through the array to check what indexes are in order, keep track of the indexes, add them and freturn the sum
    best_sum=nums[0]
    for i in range (len(nums)): 
        current_sum=0 
        for j in range (i, len(nums)):
            current_sum+=nums[j]
            if current_sum>best_sum:
                best_sum=current_sum
    return best_sum
    


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
