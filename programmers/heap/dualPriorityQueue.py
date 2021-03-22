import heapq


def solution(operations):
    count = 0
    stack_result = []
    heap_min_result, heap_max_result = [], []
    for operation in operations:  # 명령어는 앞에 위치하기 때문
        oper_command, oper_number = operation.split()
        if oper_command == 'I':  # heap push 작업
            count += 1
            stack_result.append(int(oper_number))
        elif oper_command == 'D':  # 삭제 작업
            if count == 0:  # 비어있는 큐일때
                continue
            count -= 1
            if oper_number == '-1':  # 최소값 삭제
                heap_min_result = stack_result[:]
                heapq.heapify(heap_min_result)
                stack_result.remove((heapq.heappop(heap_min_result)))

            else:  # 최대 값 삭제
                heap_max_result = list(map(lambda x: -x, stack_result[:]))
                heapq.heapify(heap_max_result)
                stack_result.remove(-(heapq.heappop(heap_max_result)))

    heap_min_result, heap_max_result = stack_result[:], list(map(lambda x: -x, stack_result[:]))
    heapq.heapify(heap_min_result)
    heapq.heapify(heap_max_result)
    if count == 0:  # 힙이 비어져 있는 경우
        return [0, 0]
    else:
        return [-(heap_max_result[0]), heap_min_result[0]]