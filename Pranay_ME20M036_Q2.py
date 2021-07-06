arr = []
n = int(input("Number of integer inputs (elements) :"))
print("please input numbers (elements) in array")
for i in range(0,n,1):
    arr.append(int(input()))
print(arr)
tar = int(input("Target value is :"))

k=1
Dict = {1: [1,2]}
for i in range(0,n,1):
    for j in range(0,n,1):
        if i!=j:
            if arr[i]+arr[j]==tar:
                Dict[k] = [i,j]
                k = k+1
print(Dict)
    
