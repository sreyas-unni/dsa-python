
def check_sorted(arr):
        sorted=True
        for i in range(0,n-1):
                if arr[i]>arr[i+1]:
                sorted=False
                break
        if(sorted==True):
                print("sorted")
        else:
                print("not sorted")
