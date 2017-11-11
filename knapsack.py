# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight_norep_dp(W, w):
    value = [[0 for wt in range(W+1)] for i in range(len(w)+1)]
    for i in range(1,len(w)+1) :
        for wt in range(1,(W+1)) :
            value[i][wt]=value[i-1][wt]                # doesn't contain item i
            if w[i-1] <= wt :                          # contain item i but need to check the weight first
                temp = value[i-1][wt-w[i-1]]+w[i-1]
                if value[i][wt] < temp :
                    value[i][wt] = temp
    #print(value)
    #return value
    return value[len(w)][W]

def optimal_weight_norep_table(value,w):
    item_num = len(value)-1
    total_wt = len(value[0])-1
    opt_sol = [0 for i in range(item_num+1)]
    final_val = value[item_num][total_wt]
    current_item = item_num
    current_wt  = total_wt
    while current_item>0 :
        if current_wt > w[current_item-1] :
            if value[current_item-1][current_wt] < value[current_item-1][current_wt-w[current_item-1]]+w[current_item-1] :
                opt_sol[current_item] = 1
                current_wt -= w[current_item-1]
            else:
                opt_sol[current_item] = 0
        current_item -= 1
    #print(opt_sol)
    return opt_sol

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #ans = optimal_weight_norep_dp(W, w)
    #opt_sol_seq = optimal_weight_norep_table(ans, w)
    #weight = sum([a * b for a, b in zip(w, opt_sol_seq[1:])])
    #print(weight)
    print(optimal_weight_norep_dp(W, w))  #starter code
