from collections import Counter, deque
import heapq

def leastInterval(tasks: list[str], n: int) -> int:
    count = Counter(tasks)
    max_heap = [-val for val in count.values()]
    heapq.heapify(max_heap)

    time = 0
    queue = deque() # pairs of [count, idle_time]

    while max_heap or queue:
        time += 1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt:
                queue.append([cnt, time + n])
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])

    return time


def main() -> None:
    print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))   # 8
    print(leastInterval(tasks = ["A","C","A","B","D","B"], n = 1))   # 6
    print(leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3))  # 10


if __name__ == '__main__':
    main()