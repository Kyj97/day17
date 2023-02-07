import random


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


memory = []
root = None
data_array = ['레쓰비캔커피', '바나나맛우유', '츄파츕스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_array = [random.choice(data_array) for i in range(20)]
print(f'오늘 판매된 물건(중복O) -->{sell_array}')

node = TreeNode()
node.data = sell_array[0]
root = node
memory.append(node)

for name in sell_array[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            break
        elif name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print("이진 탐색 트리 구성 완료!")


def preorder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


print('오늘 판매된 종류(중복X) : ', end='')
preorder(root)

