class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #예외처리
        if head is None:
            return None

        odd = head
        even = even_head = head.next
        #반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            even = even.next
            odd = odd.next
        #홀수 노드의 마지막을 짝수 헤드에 연결
        odd.next = even_head
        return head