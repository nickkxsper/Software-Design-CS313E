#  File: recursion2.py 

#  Description: Various Recursion Exercises

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 3/12/2021

#  Date Last Modified: 3/12/2021


def groupSum(start, nums, target):
    '''
    
    # Given an array of ints, is it possible to choose a group of some 
    # of the ints, such that the group sums to the given target? 
    # This is a classic backtracking recursion problem. Once you 
    # understand the recursive backtracking strategy in this problem, 
    # you can use the same pattern for many problems to search a space 
    # of choices. Rather than looking at the whole array, our convention 
    # is to consider the part of the array starting at index start and 
    # continuing to the end of the array. The caller can specify the 
    # whole array simply by passing start as 0. No loops are needed -- 
    # the recursive calls progress down the array. 
    '''
    if len(nums) <= start:
        return target == 0
    else:
        return groupSum(start + 1, nums, target) or groupSum (start + 1, nums, target - nums[start])

def groupSum6(start, nums, target):
    '''
     
    # Given an array of ints, is it possible to choose a group of some 
    # of the ints, beginning at the start index, such that the group 
    # sums to the given target? However, with the additional constraint 
    # that all 6's must be chosen. (No loops needed.)

    '''
    if len(nums) <= start:
        return target == 0
    elif nums[start] == 6 :
        return  groupSum6(start+1,nums,target-nums[start])
    else:
        return groupSum6(start+1,nums,target) or groupSum6(start+1,nums,target-nums[start])
  

def groupNoAdj(start, nums, target):
    '''
    # Given an array of ints, is it possible to choose a group of some 
    # of the ints, such that the group sums to the given target with this 
    # additional constraint: If a value in the array is chosen to be in 
    # the group, the value immediately following it in the array must 
    # not be chosen. (No loops needed.) 

    '''

    if len(nums) <= start:
        return target == 0
    else:
        return groupNoAdj(start+1,nums,target) or groupNoAdj(start+2,nums,target-nums[start])

def groupSum5(start, nums, target):
    '''
    
    # Given an array of ints, is it possible to choose a group 
    # of some of the ints, such that the group sums to the given 
    # target with these additional constraints: all multiples of 
    # 5 in the array must be included in the group. If the value 
    # immediately following a multiple of 5 is 1, it must not 
    # be chosen. (No loops needed.)

    '''
    if len(nums) <= start:
        return target == 0

    elif nums[start] % 5 == 0:
        if start<=(len(nums)-2) and nums[start+1] == 1:
            return groupSum5(start + 2, nums, target - nums[start])
        return groupSum5(start+1,nums,target-nums[start])

    else:
        return groupSum5(start + 1, nums, target) or groupSum5(start + 1, nums, target - nums[start])
  

def groupSumClump(start, nums, target):
    '''
    # Given an array of ints, is it possible to choose a 
    # group of some of the ints, such that the group sums 
    # to the given target, with this additional constraint: 
    # if there are numbers in the array that are adjacent 
    # and the identical value, they must either all be chosen, 
    # or none of them chosen. For example, with the array 
    # [1, 2, 2, 2, 5, 2], either all three 2's in the middle 
    # must be chosen or not, all as a group. (one loop can 
    # be used to find the extent of the identical values). 


    '''
    temp = start + 1

    if len(nums) <= start:
        return target == 0


    elif temp < len(nums) and nums[start] == nums[temp]:
        duplicates = nums[start]
        count = 0
        for i in range (temp + 1, len(nums)):
            if nums[i] == nums[temp]:
                count += 1
            else:
                break
        return  groupSumClump(temp + count + 1, nums, target) or groupSumClump(temp + count + 1, nums, target - duplicates*(count+2))
        
    else:
        return groupSumClump(temp, nums, target) or groupSumClump(temp, nums, target - nums[start])
  

def splitArray(nums):
    return splitArrayHelper(nums, 0, 0, 0)

def splitArrayHelper(nums, sum1, sum2, start):
    '''
    # Given an array of ints, is it possible to divide the 
    # ints into two groups, so that the sums of the two 
    # groups are the same. Every int must be in one group 
    # or the other. Write a recursive helper method that 
    # takes whatever arguments you like, and make the 
    # initial call to your recursive helper from splitArray(). 
    # (No loops needed.)

    '''
    if len(nums) <= start:
        return sum1 == sum2

    return splitArrayHelper(nums, sum1 + nums[start], sum2, start + 1) or splitArrayHelper(nums, sum1, sum2 + nums[start], start + 1)
	

def splitOdd10(nums):
    return splitOdd10Helper(nums, 0, 0, 0)
  
def splitOdd10Helper(nums, sum1, sum2, start):
    '''
    # Given an array of ints, is it possible to divide the 
    # ints into two groups, so that the sum of one group
    # is a multiple of 10, and the sum of the other group 
    # is odd. Every int must be in one group or the other. 
    # Write a recursive helper method that takes whatever 
    # arguments you like, and make the initial call to your 
    # recursive helper from splitOdd10(). (No loops needed.)

    '''
    if len(nums) <= start:
        return  ((sum2 % 10 == 0) and (sum1 % 2 == 1)) or ((sum1 % 10 == 0) and (sum2 % 2 == 1))

    return splitOdd10Helper(nums, sum1 + nums[start], sum2, start + 1) or splitOdd10Helper(nums, sum1, sum2 + nums[start], start + 1)


  

def split53(nums):
    return split53Helper(nums, 0, 0)

def split53Helper(nums, start, diff):
    '''
    # Given an array of ints, is it possible to divide the ints 
    # into two groups, so that the sum of the two groups is the 
    # same, with these constraints: all the values that are 
    # multiple of 5 must be in one group, and all the values 
    # that are a multiple of 3 (and not a multiple of 5) 
    # must be in the other. (No loops needed.) 

    #instead of creating new list. instead add all mult5s and subtract all mult3s and check if ending list sum is 0.


    '''
    if len(nums) <= start:
        return diff == 0
    temp = nums[start]

    if temp % 5 == 0:
        return split53Helper(nums, start + 1, diff + temp)

    elif temp % 3 == 0:
        return split53Helper(nums, start + 1, diff - temp)

    return split53Helper(nums, start + 1, diff - temp) or split53Helper(nums, start + 1, diff + temp) 

#######################################################################################################
#######################################################################################################
#                                                                                                     #
#                   DO NOT MODIFY ANYTHING BELOW THIS LINE !!                                         #
#                                                                                                     #
#######################################################################################################
#######################################################################################################
def main(argv):
    problems = ["groupSum", "groupSum6", "groupNoAdj", "groupSum5", "groupSumClump", "splitArray", "splitOdd10", "split53"]
    if len(argv) == 0:
        printHelp()
        exit(1)
    elif "all" in argv:
        argv = problems
    for problem in argv:
        if not problem in problems:
            printHelp()
            exit(1)
    
    groupSum_args = [(0, [2, 4, 8], 10), (0, [2, 4, 8], 14), (0, [2, 4, 8], 9), (0, [2, 4, 8], 8), (1, [2, 4, 8], 8), (1, [2, 4, 8], 2), (0, [1], 1), (0, [9], 1), (1, [9], 0), (0, [], 0), (0, [10, 2, 2, 5], 17), (0, [10, 2, 2, 5], 15), (0, [10, 2, 2, 5], 9)]
    groupSum6_args = [(0, [5, 6, 2], 8), (0, [5, 6, 2], 9), (0, [5, 6, 2], 7), (0, [1], 1), (0, [9], 1), (0, [], 0), (0, [3, 2, 4, 6], 8), (0, [6, 2, 4, 3], 8), (0, [5, 2, 4, 6], 9), (0, [6, 2, 4, 5], 9), (0, [3, 2, 4, 6], 3), (0, [1, 6, 2, 6, 4], 12), (0, [1, 6, 2, 6, 4], 13), (0, [1, 6, 2, 6, 4], 4), (0, [1, 6, 2, 6, 4], 9), (0, [1, 6, 2, 6, 5], 14), (0, [1, 6, 2, 6, 5], 15), (0, [1, 6, 2, 6, 5], 16)]
    groupNoAdj_args = [(0, [2, 5, 10, 4], 12), (0, [2, 5, 10, 4], 14), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4, 2], 7), (0, [2, 5, 10, 4], 9), (0, [10, 2, 2, 3, 3], 15), (0, [10, 2, 2, 3, 3], 7), (0, [], 0), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [5, 10, 4, 1], 11)]
    groupSum5_args = [(0, [2, 5, 10, 4], 19), (0, [2, 5, 10, 4], 17), (0, [2, 5, 10, 4], 12), (0, [2, 5, 4, 10], 12), (0, [3, 5, 1], 4), (0, [3, 5, 1], 5), (0, [1, 3, 5], 5), (0, [3, 5, 1], 9), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4], 15), (0, [2, 5, 10, 4], 11), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [], 0)]
    groupSumClump_args = [(0, [2, 4, 8], 10), (0, [1, 2, 4, 8, 1], 14), (0, [2, 4, 4, 8], 14), (0, [8, 2, 2, 1], 9), (0, [8, 2, 2, 1], 11), (0, [1], 1), (0, [9], 1)]
    splitArray_args = [([2, 2]), ([2, 3]), ([5, 2, 3]), ([5, 2, 2]), ([1, 1, 1, 1, 1, 1]), ([1, 1, 1, 1, 1]), ([]), ([1]), ([3, 5]), ([5, 3, 2]), ([2,2,10,10,1,1]), ([1,2,2,10,10,1,1]), ([1,2,3,10,10,1,1])]
    splitOdd10_args = [[5, 5, 5], [5, 5, 6], [5, 5, 6, 1], [6, 5, 5, 1], [6, 5, 5, 1, 10], [6, 5, 5, 5, 1], [1], [], [10, 7, 5, 5], [10, 0, 5, 5], [10, 7, 5, 5, 2], [10, 7, 5, 5, 1]]
    split53_args = [[1,1], [1, 1, 1], [2, 4, 2], [2, 2, 2, 1], [3, 3, 5, 1], [3, 5, 8], [2, 4, 6], [3, 5, 6, 10, 3, 3]]
	
	
    groupSum_ans = [True, True, False, True, True, False, True, False, True, True, True, True, True]
    groupSum6_ans = [True, False, False, True, False, True, True, True, False, False, False, True, True, False, False, True, True, False]
    groupNoAdj_ans = [True, False, False, True, True, True, False, True, True, False, True, True]
    groupSum5_ans = [True, True, False, False, False, True, True, False, False, True, False, True, False, True, True]
    groupSumClump_ans = [True, True, False, True, False, True, False]
    splitArray_ans = [True, False, True, False, True, False, True, False, False, True, True, False, True]
    splitOdd10_ans = [True, False, True, True, True, False, True, False, True, False, True, False]
    split53_ans = [True, False, True, False, True, False, True, True]

    for prob in argv:
      correct = 0  # counts number of test cases passed
      leftParen = "("
      rightParen = ")"
      # loop over test cases
      for i in range(len(locals()[prob+"_args"])):
        if type(locals()[prob+"_args"][i]) is tuple:
          leftParen = rightParen = ""
        if (type(locals()[prob+"_args"][i]) is str) or (type(locals()[prob+"_args"][i]) is int) or (type(locals()[prob+"_args"][i]) is list) or (len(locals()[prob+"_args"][i]) == 1): # function takes one argument
          if globals()[prob](locals()[prob+"_args"][i]) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
        elif len(locals()[prob+"_args"][i]) == 2: # there are two arguments to function
          first, second = locals()[prob+"_args"][i]
          if globals()[prob](first, second) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWorng!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
        else:    
          first, second, third = locals()[prob+"_args"][i]
          if globals()[prob](first, second, third) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
      print ("\n" + prob + ": passed", correct, "out of", len(locals()[prob+"_ans"]), "\n")

def printHelp():
    print ("\nInvoke this script with the name of the function you wish to test.")
    print ("e.g. python recursion1.py factorial")
    print ("Invoke with \"python recursion1.py all\" to run all of the function tests\n")
      
import sys
main(sys.argv[1:])