lst = ["Max", "Ali", "Diboya","Cate", "John"]
print(lst)
new_lst = [i for i in lst]
print([i.upper() for i in new_lst])
print([i.lower() for i in new_lst])

st = set()
for i in range(5):
    st.add(int(input(f"Enter an item {i+1}")))
    print(st)
for i in st:
    if i%2 != 0:
        print(i)