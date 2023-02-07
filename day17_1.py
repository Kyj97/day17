def is_queue_empty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def de_queue():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print(f'대기 줄 상태 : {queue}\n식당 영업 종료!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front + 1, SIZE):
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1

    return data


SIZE = 5
queue = ["정국", "뷔", "지민", "진", "슈가"]
front = -1
rear = 4
i = 0

while True:
    print(f'대기 줄 상태 : {queue}')
    print(f'{de_queue()} 님 식당에 들어감')
    i = i + 1

    if i == SIZE:
        de_queue()
        break