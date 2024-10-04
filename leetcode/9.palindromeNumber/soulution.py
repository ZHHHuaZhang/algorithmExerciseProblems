
def isPalindrome(x: int) -> bool:
    #if str(x)[::-1] == str(x): 这一行是函数的核心。首先，str(x)将整数x转换为字符串。
    # 然后，[::-1]是Python中的切片操作，用于反转字符串。具体来说，[start:stop:step]是一个切片操作，
    # 其中start是起始索引（默认为0），stop是结束索引（默认为字符串长度，但不包括该索引处的字符），
    # step是步长（默认为1）。在这里，没有指定start和stop，但指定了step为-1，
    # 表示从字符串的末尾开始向前遍历，直到字符串的开头，即实现了反转。
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

def isPalindrome_v2(x: int) -> bool:
        if(x<0 or (x%10==0 and x != 0)):
            return False
        
        revertedNumber:int = 0
        
        while(x > revertedNumber):
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        return x == revertedNumber or x == revertedNumber // 10

    
print(isPalindrome(121))
