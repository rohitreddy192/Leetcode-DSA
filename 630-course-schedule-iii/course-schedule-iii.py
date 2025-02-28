import heapq

class Solution:
    def scheduleCourse(self, courses):
        # Step 1: Sort courses by deadline
        courses.sort(key=lambda x: x[1])  
        
        max_heap = []  # Max heap (simulated using negative values)
        time = 0

        # Step 2: Iterate over courses
        for duration, deadline in courses:
            if time + duration <= deadline:  
                heapq.heappush(max_heap, -duration)  # Use negative to simulate max heap
                time += duration  
            elif max_heap and -max_heap[0] > duration:
                time += duration + heapq.heappop(max_heap)  # Replace longest course
                heapq.heappush(max_heap, -duration)
        
        return len(max_heap)  # Total courses taken