from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next # 次のノードを一時保存
            current.next = prev # 向きを逆にする
            prev = current # prevを進める
            current = next_node # currentを進める
        
        return prev