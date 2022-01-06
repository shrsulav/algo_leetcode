def coin_row(row):
    if(len(row) == 0):
        return 0
    
    if(len(row) == 1):
        return row[0]
    
    value_table = [0, row[0]]
    last_value_table = [True]
    if(len(row) > 1):
        if(row[1] > row[0]):
            value_table.append(row[1])
            last_value_table.append(True)
        else:
            value_table.append(row[0])
            last_value_table.append(False)
    for i in range(2, len(row)):
        value_with_last = row[i] + value_table[i - 1]
        value_wo_last = value_table[i]
        if(value_with_last > value_wo_last):
            value_table.append(value_with_last)
            last_value_table.append(True)
        else:
            value_table.append(value_wo_last)
            last_value_table.append(False)
    print(row)
    value_table.pop(0)
    print(value_table)
    print(last_value_table)
    return value_table[-1]

if __name__ == '__main__':
    print(coin_row([5,1,2,10,6,2]))