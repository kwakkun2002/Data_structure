class LruCacheList:
    def __init__(self, capacity: int):
        self.cache = []
        self.size = 0
        self.capacity = capacity

    def append(self, p):
        if p in self.cache:  # cache hit!! => remove p and push
            self.cache.remove(p)
            self.cache.append(p)
            return "CACHE HIT"
        elif self.size < self.capacity:  # cache miss... => append p
            self.cache.append(p)
            self.size += 1
            return "CACHE MISS"
        else:  # size overflow!! => remove lru
            self.cache.pop(0)
            self.cache.append(p)
            return "SIZE OVERFLOW"

    def view(self):
        print(self.cache)

    def get_lru_value(self):
        return self.cache[0]

    def get_mru_value(self):
        return self.cache[-1]


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
