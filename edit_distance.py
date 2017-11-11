# Uses python3
def edit_distance(s, t):
    #write your code here
    len1 = len(s)
    len2 = len(t)
    #print("len1=" , len1 , "len2= " , len2 )
    dist = [[0 for j in range(len2+1)] for i in range(len1 + 1)]
    for i in range(1,len1+1):
        dist[i][0] = i
    for j in range(1,len2+1):
        dist[0][j] = j
    #print(dist)
    for j in range(1,len2+1) :
        for i in range(1,len1+1) :
            #print("i= " , i , "j= " , j)
            insertion = dist[i]  [j-1] +1
            #print("insertaion: " , insertion)
            deletion  = dist[i-1][j]   +1
            #print("deletion: " , deletion )
            match     = dist[i-1][j-1]
            #print("match: " , match)
            mismatch  = dist[i-1][j-1] +1
            #print("mismatch: " , mismatch)
            if s[i-1] == t[j-1] :
                dist[i][j] = min(insertion,deletion,match)
            else:
                dist[i][j] = min(insertion,deletion,mismatch)
            #print(dist)
    #print(dist)
    #print(dist[len1][len2])
    return dist[len1][len2]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
