'''
1. Given a list of n natural numbers ranging between 1 and 1,000,000,000,
find the most popular k scores in the descending order of their frequency.
Input: n = 11, k = 3, numbers = [6, 5, 2, 6, 6, 2, 1, 7, 3, 3, 3] Output: [6, 3, 2]

'''
def takeSecond(elem):
    return elem[1]

if __name__ == "__main__":
    n = 11
    k = 3
    numbers = [6, 5, 2, 6, 6, 2, 1, 7, 3, 3, 3]
    output = []

    for i in range(0, n):

        # if is in list output
        p = 0; b = 0
        for j in range(len(output)):
            if(numbers[i] == output[j][0]):
                if(p == 0):
                    b = j
                p = 1; break

        if(p == 0): # if isn't in list output
            output.append([numbers[i], 1])
        else:
            output[b][1] = output[b][1] + 1 # 0 freq -> 1

        
    
    # ordonare dupa frecventa
    output.sort(key=takeSecond, reverse=True)

    # printare required
    result = []
    for i in range(k):
        result.append(output[i][0])
    
    print(result)