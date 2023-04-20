
def check_substr(string: str) -> int:
    if not string:
        return 1 
    
    unique = set()
    left = 0 
    ans = 0
    
    for right in range(len(string)):
        while string[right] in unique:
            unique.remove(string[left])
            print(unique)
            left += 1 

        unique.add(string[right])
        print(unique)
        print(right,left)
        ans = max(ans, right - left + 1)
        
        
    return ans
            
if __name__ == '__main__':
    string = str(input())
    print(check_substr(string))



