data = [[5,3],[22,11,1],[0,4],[2,3,4,5,6]]
# each list item ko total naya list ma chaiyo
for one_list in data:
    total = 0 
    for item in one_list:
        total = total + item 
    print(total)
