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

X = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '3', '19', '20', '21', '13', '22', '23', '24', '8', '25', '26', '27', '28', '29', '30', '14', '15', '13', '3', '19', '20', '21', '25', '8', '22', '23', '31', '26', '27', '32', '29', '33', '34', '35', '36', '37', '8', '9', '38', '39', '40', '3', '41', '34', '36', '35', '42', '43', '8', '44', '45', '46', '47', '48', '49', '50', '51', '52', '8', '5', '4', '53', '48', '47', '54', '3', '55', '56', '29', '10', '57', '58', '59', '60', '48', '47', '25', '8', '51', '61', '62', '63', '64', '65', '66', '67', '68']
Y = ['32', '10', '75', '41', '65', '67', '76', '38', '39', '77', '78', '34', '79', '50', '80', '81', '82', '14', '83', '84', '32', '60', '30', '85', '8', '25', '77', '38', '39', '86', '87', '78', '88', '7', '89', '85', '90', '91', '92', '93', '78', '8', '25', '94', '11', '12', '85', '34', '95', '96', '97', '78', '3', '25', '8', '51', '98', '99', '10', '100', '101', '3', '47', '61', '34', '85', '97', '96', '92', '78', '94', '102', '7', '95', '91', '3', '97', '96', '78', '94', '25', '8', '32', '43', '3', '95', '103', '47', '48', '94', '97', '96', '78', '10', '8', '37', '3', '34', '45', '46']

m = len(X)
n = len(Y)

# `T[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
T = [[0 for x in range(n + 1)] for y in range(m + 1)]

# fill lookup table
LCSLength(X, Y, m, n, T)

# find the longest common sequence
print(LCS(X, Y, m, n, T))
print(len(LCS(X, Y, m, n, T)))