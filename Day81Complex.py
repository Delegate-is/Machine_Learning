# program to get 5 no and store in list, then convert to pandas series to change default indexes to alpha
import pandas as pd
list_1 = []
for i in range(5):
    list_1.append(i)
    print(list_1)
ps = pd.Series(list_1)
print("Pandas Items" +str(ps))
ps_ = pd.Series(list_1, index=['a','b','c','d','e'])
print(ps_)