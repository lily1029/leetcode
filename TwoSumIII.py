class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.counter = {}
        
    def add(self, number):
        # write your code here
        self.counter[number] = self.counter.get(number, 0) + 1 

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, target):
        # write your code here
        for key in self.counter:
            if target - key in self.counter and target != key * 2:
                return True 
            if target == key * 2 and self.counter[key] >= 2:
                return True
        return False

if __name__ == '__main__':
    ll = TwoSum()
    x = ll.add(1)
    y = ll.add(3)
    z = ll.add(5)
    q = ll.find(4)
    w = ll.find(7)
    print(q)
    print(w)
    
    
