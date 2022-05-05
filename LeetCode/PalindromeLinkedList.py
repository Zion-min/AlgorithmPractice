class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        '''
         #개수 저장 왜 따로 변수 길이 저장하면 안되냐
        #이런 문제가 아니었음.. return 타입 확인 제대로 안하고 문자열로 반환한 탓..
        node = head
        li = []
        
        while node:
            li.append(node.val)
            node = node.next
        
        #노드 개수 홀수면 바로 false return => 매우매우 오류임;
        #노드 개수가 홀수인데 1이면 true임;;;;
        #아 노드 개수 홀수여도 대눈군아
        #if랑 else 뒤에 : 붙이는거 잊지 않기
        
        #python은 &&이 and임
        #결국 경우의 수는, 노드 개수 1인경우, 짝수인 경우, 홀수인경우로 나누어 생각 가능
        
        nodelen = len(li) // 2
        
        if len(li)==1:
            return True
        if (len(li) % 2==0) and (li[nodelen-1::-1] == li[nodelen:]):
            return True   
        if (len(li) % 2) and (li[nodelen-1::-1] == li[nodelen+1:]):
            return True
        '''
        
        #매우 잘못 생각한 부분.. 결국 Palindrome Linked list는 반잘라서 확인이 아니고.. 뒤집어도 같은거임
        node = head
        li = []
        
        while node:
            li.append(node.val)
            node = node.next
    
        return li[::-1]==li
        
