from heapq import heappush, heappop

class NumberContainers:
    def __init__(self):
        self.index_to_num = {}  # maps index -> number
        self.num_to_indices = {}  # maps number -> min heap of indices
        
    def change(self, index: int, number: int) -> None:
        # Remove old number if exists
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            # Don't remove from heap - we'll handle stale entries in find()
            
        # Add new number
        self.index_to_num[index] = number
        if number not in self.num_to_indices:
            self.num_to_indices[number] = []
        heappush(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_indices:
            return -1
            
        # Keep popping until we find an index that still has this number
        while self.num_to_indices[number]:
            min_idx = self.num_to_indices[number][0]  # Peek at smallest
            if min_idx in self.index_to_num and self.index_to_num[min_idx] == number:
                return min_idx
            heappop(self.num_to_indices[number])  # Remove stale entry
            
        return -1