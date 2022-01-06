def knapsack(weights, values, W):
    if(W==0):
        return 0
    
    if(len(weights) == 0):
        return 0
    
    table = []
    for i in range(0,W+1):
        table.append([0])
        for j in range(len(weights)):
            curr_length = j
            # print('items: ', j, ' weights: ', weights[j], ' values: ', values[j])
            val = None
            if(i >= weights[curr_length]):
                val1 = table[i][curr_length]
                val2 = table[i-weights[curr_length]][curr_length] + values[curr_length]
                if(val1 > val2):
                    val = val1
                else:
                    val = val2
            else:
                val = table[i][curr_length]
            print(val)
            table[i].append(val)
    print('Weights:')
    print(weights)
    print('Values:')
    print(values)
    print('Table:')
    for v, row in enumerate(table):
        print(v, ':', row)
    print(table[-1][-1])
    find_weights(table, weights, values, W)

def find_weights(table, weights, values, W):
    weight_composition = []
    value_composition = []
    t_weight = W
    num_items = len(weights)
    # print(len(table[W]))
    # print(table[5][5])
    while(t_weight>0):
        if(table[t_weight][num_items] > table[t_weight][num_items-1]):
            weight_composition.append(weights[num_items-1])
            value_composition.append(values[num_items-1])
            t_weight -= weights[num_items-1]

        num_items -= 1
    print(weight_composition)
    print(value_composition)

if __name__ == '__main__':
    # knapsack([2,1,3,2], [12,10,20,15], 5)
    knapsack([3,2,1,4,5], [25,20,15,40,45],6)