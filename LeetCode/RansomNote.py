class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazin_count = { i:0 for i in set(magazine)}
        ransomNote_count = { i:0 for i in set(ransomNote)}
        
        for i in magazine:
            magazin_count[i]+=1
            
        for i in ransomNote:
            ransomNote_count[i]+=1
            
        
        for x in ransomNote_count : 
            if magazin_count.get(x) != None:
                if ransomNote_count[x]>magazin_count[x] : 
                    return False
            else:
                return False
            
        return True
        
        
        
        """
        근데 예외가 발생하니까 시간 더 걸림
        magazin_count = { i:0 for i in set(magazine)}
        ransomNote_count = { i:0 for i in set(ransomNote)}
        
        for i in magazine:
            magazin_count[i]+=1
            
        for i in ransomNote:
            ransomNote_count[i]+=1
            
        
        for x in ransomNote_count : 
            try:
                if ransomNote_count[x]>magazin_count[x] : 
                    return False
            except:
                return False
            
        return True
        
        
        """
        """
        뭔가 get이 시간을 잡아먹는듯하다. 
        magazin_count = { i:0 for i in set(magazine)}
        ransomNote_count = { i:0 for i in set(ransomNote)}
        
        for i in magazine:
            magazin_count[i]+=1
            
        for i in ransomNote:
            ransomNote_count[i]+=1
            
        
        for x in ransomNote_count : 
            if magazin_count.get(x) != None:
                if ransomNote_count[x]>magazin_count[x] : 
                    return False
            else:
                return False
            
        return True
        """
        
    
        """
        from collections import Counter
        
        magazin_count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)
    
        
        
        for x in ransomNote_count : 
            if ransomNote_count[x]>magazin_count[x] : 
                return False
            
        return True
        """

    
    
    
    
    
        """        
        ransomCount = {}
        magazineCount = {}
        
        for i in list(ransomNote):
            if ransomCount.get(i) !=None:
                ransomCount[i] +=1
            else:
                ransomCount[i]= 1
        
        for i in list(magazine):
            if magazineCount.get(i)!=None:
                magazineCount[i] +=1
            else:
                magazineCount[i]= 1
                
        
        for i in ransomCount.keys():
            if magazineCount.get(i) != None:
                if ransomCount[i] > magazineCount[i]:
                    return False
            else:
                return False
                
        return True
        """
        
        
        
        """
        li1 = list(magazine)
        li2 = list(ransomNote)
        
        for i in li1:
            if i in li2:
                li2.remove(i)

        if len(li2) >= 1:
            return False

        return True

        """     
        
        
        
"""
랜섬노트가 매거진으로부터 생성될 수 있으면 true, 아니면 false
매거진의 각 단어는 랜섬노트에서 한번만 사용가능
매거진 aab가 주어지면, 랜섬노트 a, aa, aab, aba 뭐 이런거 생성 가능

순열? 모든 순열 만들어 놓고 있는지 검사?

매거진꺼 한개씩 꺼내면서 
랜섬노트에 있으면 제거 
없으면 넘어가기

마지막에 랜섬노트 배열 원소 길이가 1이상이면 False 반환

""" 
"""
개선)
파이썬에서는 if i in li2여기서, 리스트 전체를 다 돌고 리무브를 함. 그래서 이중포문이라서 O(n^2)이 나옴 
그래서 !! a, b등 원소의 개수를 세서 딕셔너리를 생성해줌.
그걸로 만약 랜섬노트의 원소의 개수가 더 많으면 false 반환. 돌면서 검사하다가 아니면 바로 나오는 거라서, 시간이 더 단축될 수도 있음. 

"""
