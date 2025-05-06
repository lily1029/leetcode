from typing import List
import heapq

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Solution:
    def kClosest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        #we initiaize a heap
        self.heap = []

        #here we loop through all the points
        for point in points:
            #here we use .get_distance method to figure out how long the distance from 
            #this point to the origin
            dist = self.get_distance(point, origin)

            #then, we push the point to the heapq, here, we use - , because it is 
            #min heap 
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))

            #here we only want to find k closest points, so we compare the length and k
            #so if length > k, we pop out the bigger one
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        
        # here we restore the final result
        ret = []

        # here is the last results, we append the points with positive numbers
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))
        
        # reverse and make it from smaller to bigger
        ret.reverse()
        return ret 
    
    # 这里是二位平面求两个点的距离
    def get_distance(self, a: Point, b: Point) -> int:
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

if __name__ == '__main__':
    point1 = Point(4, 6)
    point2 = Point(4, 7)
    point3 = Point(4, 4)
    point4 = Point(2, 5)
    point5 = Point(1, 1)

    points = [point1, point2, point3, point4, point5]
    origin = Point(0, 0)
    k = 3
    ll = Solution()
    x = ll.kClosest(points, origin, k)
    print(x)
