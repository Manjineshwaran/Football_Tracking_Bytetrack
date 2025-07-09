n={
    "player":[],
    "refree":[]
}
print("\n n = ", n)
print("\n n[player] = ",n["player"])

n["player"].append({})
n["refree"].append({})

print("\n n = ", n)
print("\n n[player] = ",n["player"])

for i in range(2):
    n["player"][0][i] = {"bbox":[1,2,3,4]}

print("\n n = ", n)
print("\n n[player] = ",n["player"])