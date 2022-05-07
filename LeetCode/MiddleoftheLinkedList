# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        count = 0
        
        while node:
            count += 1
            node = node.next
        
        #링크드 리스트는 한번 탐색하면 끝에 가있어서 포인터를 다시 돌려놔줘야 함.
        node = head
        
        for i in range(count):
            if i >= count//2:
                return node
            node = node.next
            
        
        
        
    
#리턴 타입 제대로 확인 안할래,, list로 착각
#예외 케이스 꼼꼼히 따지기. 

"""
만약 fast가 끝에 도달했으면, slow는 middle에 있음. 우왕 신기해.... ㅋㅋㅋㅋ
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
"""
