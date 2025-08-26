import heapq

h=[]
heapq.heapify(h) #min heap the minimum value is at the top
print(h)
heapq.heappush(h,5)
print(h)
heapq.heappush(h,1)
print(h)
heapq.heappush(h,3)
print(h)
heapq.heappush(h,7)
print(h)
print(heapq.heappop(h)) #1
print(h)
print(heapq.nlargest(2,h)) #[7,5]
print(h)