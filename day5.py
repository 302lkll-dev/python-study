budgets=["1,200","3,400","2,100"]
clean=[]
for b in budgets:
    b=int(b.replace(",",""))
    clean.append(b)
print(sum(clean)/len(clean))

budgets = [1200, 3400, 2100]

for b in budgets:
    print(f"예산: {b}원")