    a = [x for x in arr[l:mid+1]]
        b = [x for x in arr[mid+1: r+1]]
        i, j, k = 0, 0, l
        while k <= r:
            if j == len(b):
                arr[k] = a[i]
                i += 1
                k += 1
            elif i == len(a):
                arr[k] = b[j]
                j += 1
                k += 1
            elif a[i] < b[j]:
                arr[k] = a[i]
                i += 1
                k += 1
            else:
                arr[k] = b[j]
                j += 1
                k += 1      