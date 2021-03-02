from csv import reader

## WE ARE USING LCS CODE FROM : https://www.techiedelight.com/longest-common-subsequence-finding-lcs/ 
# Function to find the longest common subsequence of string `X[0…m-1]` and `Y[0…n-1]`
def LCS(X, Y, m, n, T):
 
    # return an empty string if the end of either sequence is reached
    if m == 0 or n == 0:
        return list()
 
    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        # append current character (`X[m-1]` or `Y[n-1]`) to LCS of
        # substring `X[0…m-2]` and `Y[0…n-2]`
        return LCS(X, Y, m - 1, n - 1, T) + [X[m - 1]]
 
    # otherwise, if the last character of `X` and `Y` are different
 
    # if a top cell of the current cell has more value than the left
    # cell, then drop the current character of string `X` and find LCS
    # of substring `X[0…m-2]`, `Y[0…n-1]`
 
    if T[m - 1][n] > T[m][n - 1]:
        return LCS(X, Y, m - 1, n, T)
    else:
        # if a left cell of the current cell has more value than the top
        # cell, then drop the current character of string `Y` and find LCS
        # of substring `X[0…m-1]`, `Y[0…n-2]`
        return LCS(X, Y, m, n - 1, T)


# read csv file as a list of lists
with open('test.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    malware = list(csv_reader)
    
threshold = 2
clusterCounter = 0
clusterIdentifier = []
labels = []
for i in range(0,len(malware)):
    a = (malware[i][2]).split("_")
    malware[i].remove(malware[i][2])
    malware[i].append(a)
    if (i == 0):
        clusterCounter = clusterCounter + 1
        clusterIdentifier.append([malware[i][2],clusterCounter])
        labels.append(clusterCounter)
    else:
        for j in range(0, len(clusterIdentifier)):
            X = clusterIdentifier[j][0]
            Y = malware[i][2]
            m = len(X)
            n = len(Y)
            T = [[0 for x in range(n + 1)] for y in range(m + 1)]
            lcs = LCS(X, Y, m, n, T)
            #print(Y)
            print(len(lcs))
            lenLCS = len(lcs)
            if (lenLCS >= threshold):
                clusterIdentifier[j][0] = lcs
                labels.append(clusterCounter)
            else:
                clusterCounter = clusterCounter + 1
                clusterIdentifier.append([malware[i][2],clusterCounter])
                labels.append(clusterCounter)

 
# Function to fill the lookup table by finding the length of LCS
# of substring `X[0…m-1]` and `Y[0…n-1]`
def LCSLength(X, Y, m, n, T):
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

X = malware[0][2]
Y = malware[1][2]
m = len(X)
n = len(Y)

# `T[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
T = [[0 for x in range(n + 1)] for y in range(m + 1)]

# fill lookup table
LCSLength(X, Y, m, n, T)

# find the longest common sequence
#print(LCS(X, Y, m, n, T))
print(len(LCS(X, Y, m, n, T)))