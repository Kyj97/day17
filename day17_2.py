import random


def is_queue_full():
    global SIZE, d_array, front, rear
    if ((rear + 1) % SIZE == front):
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, d_array, front, rear
    if (front == rear):
        return True
    else:
        return False


def en_queue(data):
    global SIZE, d_array, front, rear
    if (is_queue_full()):
        print(f'최종 대기 콜--> {d_array}\n프로그램 종료!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def de_queue():
    global SIZE, d_array, front, rear
    if (is_queue_empty()):
        return None
    front = (front + 1) % SIZE
    data = d_array[front]
    d_array[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % SIZE]


SIZE = 6
data_array = [('사용', 9), ('고장', 3), ('환불', 4), ('기타', 1)]
d_array = [random.choice(data_array) for i in range(6)]
print(d_array)
queue = [None for _ in range(SIZE)]
front = rear = 0

time = 0

for i in range(1, SIZE+1):
    print(f'귀하의 대기 예상시간은 {time}분 입니다.')
    print(f'현재 대기 콜 : {queue}')

    data = d_array[i-1]
    en_queue(data)

    if i == SIZE:
        continue
    else:
        time = time + queue[i][1]
