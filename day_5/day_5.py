#LOADING DATA
data = open('day_5.txt', 'r')


#PART 1
rows = []
cols = []
for line in data:
    #calculating rows
    row = line[:7]
    convertion = row.maketrans("FB", "01")
    binary_rows = row.translate(convertion)
    rows.append(int(binary_rows,2))

    #calculating cols
    column = line[7:]
    convertion_1 = column.maketrans("LR", "01")
    binary_cols = column.translate(convertion_1)
    cols.append(int(binary_cols, 2))

#calculating ids 
ids = []
rows_and_cols = zip(rows, cols)
for items in rows_and_cols:
    ids.append(items[0] * 8 + items[1])

print(max(ids))


#PART 2
maxi = int(max(ids))
mini = int(min(ids))

ascending = sorted(ids)
check = []
for num in range(mini, maxi):
    if num not in ascending:
        print(num)




