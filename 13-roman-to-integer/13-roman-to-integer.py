class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        li = list(s)
        pass_flag = 0
        for i, v in enumerate(li):
            if pass_flag == 1:
                pass_flag = 0
                continue
            else:
                print(i, v, answer)
                if v == 'I':
                    if i < len(li)-1:
                        if li[i+1] == 'V':
                            pass_flag = 1
                            answer += 4
                        elif li[i+1] == 'X':
                            pass_flag = 1
                            answer += 9
                        else:
                            answer += 1
                    else:
                        answer += 1
                elif v == 'V':
                    answer += 5
                elif v == 'X':
                    if i < len(li)-1:
                        if li[i+1] == 'L':
                            pass_flag = 1
                            answer += 40
                        elif li[i+1] == 'C':
                            pass_flag = 1
                            answer += 90
                        else:
                            answer += 10
                    else:
                        answer += 10
                elif v == 'L':
                    answer += 50
                elif v == 'C':
                    if i < len(li)-1:
                        if li[i+1] == 'D':
                            pass_flag = 1
                            answer += 400
                        elif li[i+1] == 'M':
                            pass_flag = 1
                            answer += 900
                        else:
                            answer += 100
                    else:
                        answer += 100
                elif v == 'D':
                    answer += 500
                elif v == 'M':
                    answer += 1000
        else:
            return answer
        
                    
        