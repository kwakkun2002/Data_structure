class CustomNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CustomLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr
            curr = curr.next

    def __contains__(self, item):
        for curr in self:
            if curr.value == item:
                return True
        return False

    def append(self, value):
        if self.head is None:  # 비어있으면 초기화
            self.head = CustomNode(value)
            self.tail = self.head
        else:  # 없으면 새로 생성
            new_node = CustomNode(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        if self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        for curr in self:
            if curr.value == value:
                prev_node = curr.prev
                next_node = curr.next
                prev_node.next = next_node
                next_node.prev = prev_node
                return

    def pop(self, idx):
        curr = self.head
        for i in range(idx):
            curr = curr.next
        if curr == self.head:
            self.head = self.head.next
        elif curr == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev_node = curr.prev
            next_node = curr.next
            prev_node.next = next_node
            next_node.prev = prev_node


class LruCacheList:
    def __init__(self, capacity: int):
        self.cache = CustomLinkedList()
        self.size = 0
        self.capacity = capacity

    def append(self, p):
        if p in self.cache:  # cache hit!! => remove p and push
            self.cache.remove(p)
            self.cache.append(p)
            # print("CACHE HIT")
            return "CACHE HIT"
        elif self.size < self.capacity:  # cache miss... => append p
            self.cache.append(p)
            self.size += 1
            # print("CACHE MISS")
            return "CACHE MISS"
        else:  # size overflow!! => remove lru
            self.cache.pop(0)
            self.cache.append(p)
            # print("SIZE OVERFLOW")
            return "SIZE OVERFLOW"


class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache_hit = 0
        self.tot_cnt = 0
        self.lru_cache_list = LruCacheList(cache_slots)

    def do_sim(self, page):
        event = self.lru_cache_list.append(page)
        if event == "CACHE HIT":
            self.cache_hit += 1
        self.tot_cnt += 1

    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ",
              self.cache_hit / self.tot_cnt)


if __name__ == "__main__":
    data_file = open("./linkbench.trc")
    lines = data_file.readlines()
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0]
            cache_sim.do_sim(page)

        cache_sim.print_stats()
