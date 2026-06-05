class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ptr = 0
        s = []
        while ptr<len(tokens):
            
            head = tokens[ptr]
            try:
                num = eval(head)
                s.append(num)
         
            except Exception as e:
                print(s, head)
                right, left = s.pop(), s.pop()
                s.append(int(eval(f"{left}{head}{right}")))
               
            ptr+=1
        return s[0]
        