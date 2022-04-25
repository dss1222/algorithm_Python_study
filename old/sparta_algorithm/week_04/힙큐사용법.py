# heapq.heappush(heap, item) # item을 heap에 추가
# heapq.heappop(heap) # heap에서 가장 작은 원소를 pop 비어있는 경우 Index Error 발생
# heapq.heapify(x) # 리스트 x를 즉각적으로 heap으로 변환함 (O(N) 시간복잡도 발생)

import heapq #파이썬의 힙큐는 최소힙으로 구현 돼있음

heap = []
heapq.heappush(heap,50)
heapq.heappush(heap,10)
heapq.heappush(heap,20)

print(heap)

heap2 = [50, 10, 20]
heapq.heapify(heap2)

print(heap2)

result = heapq.heappop(heap)
print(result)
print(heap)

result2 = heap[0] #원소를 제거하지 않고 가져오는 것 <heapq에선 한칸씩 땡김>
print(result2)
print(heap)


heap_items = [1,3,5,7,9]
max_heap = []
for item in heap_items: #맥스힙으로 바꾸는 트릭
  heapq.heappush(max_heap, (-item, item)) #이 형태로 넣어주면 첫 번째 원소를 우선순위로 힙을 구성하게된다.

print(max_heap)

max_item = heapq.heappop(max_heap)[1] #힙에 있는 최대값이 반환되는것을 확인할 수 있다. 이때 실제 원소값은 튜플의 두번째 자리에 저장돼있으므로 [1] 인덱싱으로 접근
print(max_item)


