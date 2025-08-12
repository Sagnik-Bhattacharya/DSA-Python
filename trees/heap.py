import heapq

h=[]
heapq.heapify(h) #min heap the minimum value is at the top
heapq.heappush(h,5)
heapq.heappush(h,1)
heapq.heappush(h,3)
heapq.heappush(h,7)

print(heapq.heappop(h)) #1
print(heapq.nlargest(2,h)) #[7,5]