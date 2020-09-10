import sys

def memoized_cut_rod(price, length, MaxRev, CutCost, NumCuts, LargestIndexArray) -> int:
    #if MaxRev[length] is already calculated, just return it
    if (int(MaxRev[length]) > 0):
        return MaxRev[length]
    #My base case, if length equals 0 then just return 0
    if (int(length) == 0):
        NumCuts[0] = 0
        return 0
    count = 1
    largestIndex = -1
    largest = 0
    cuts = 0
    while (count <= length):
        # if count equals length, then that means we are not cutting the rod at all, which is why it does not include  "- (CutCost * (1 + NumCuts[length - count]))"
        if (count == length):
            temp = int(price[count]) + int(memoized_cut_rod(price, (length-count), MaxRev, CutCost, NumCuts, LargestIndexArray))   
        else:
            temp = int(price[count]) + int(memoized_cut_rod(price, (length-count), MaxRev, CutCost, NumCuts, LargestIndexArray)) - (CutCost * (1 + NumCuts[length - count]))
        if (int(temp) > largest):
            largestIndex = count
            largest = temp
        count = count + 1
    if (largestIndex == length):
        cuts = 0
    else:
        cuts = 1 + NumCuts[length - largestIndex]
    #updates arrays before returning
    MaxRev[length] = largest
    NumCuts[length] = cuts
    LargestIndexArray[length] = largestIndex
    return largest
    
#Checks to make sure program received file name
if (len(sys.argv) < 2):
    sys.exit("No command line argument")
FileName = sys.argv[1]
File = open(FileName, "r")

#Makes sure file opens properly
if (File.mode != 'r'):
    print("Error opening file")

#reads in data from file into its proper variable
length = (int(File.readline().rstrip()))
CutCost = (int(File.readline().rstrip()))
temp = (File.readline().rstrip())

#define all variables that are needed
count = 0
price = [] 
start = 0 # variable used to translate file string to int
MaxRev = [] # array that maps rod length to the optimal revenue
NumCuts = [] #array that maps rod length to the number of cuts needed to get optimal revenue
LargestIndexArray = [] #array that maps rod length to the index i, which gives the largest value to the equation price[i] + MaxRev[length - i]

# both while loops below initializes my arrays values
price.append(0)
while (count < len(temp)):
    if (temp[count] == ','):
        price.append(temp[start:count])
        start = count+1
    count = count + 1
price.append(temp[start:count])
count = 0
while (count <= len(price)):
    MaxRev.append(0)
    NumCuts.append(-1)
    LargestIndexArray.append(-1)
    count = count + 1

#call to my function that calculates everything
MaxRev[length] = memoized_cut_rod(price, length, MaxRev, CutCost, NumCuts, LargestIndexArray)

#prints out results
print("My name is Ronnie Clark, and the optimal revenue for rod at length ", end = str(length))
print(" is " , end = str(MaxRev[length]))
print(", and the number of cuts for optimal revenue is ", end = str(NumCuts[length]))
print(", giving you 1 rod at length ", end = str(LargestIndexArray[length]))
count = length - LargestIndexArray[length]
while (count > 0):
    print(", plus 1 rod at length ", end = str(count))
    count = count - LargestIndexArray[count]
        
        
        
        
        
        
        
        
        
        
        