class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:  # 树叉小于节点
            if self.left is None:  # 并且左面的树叉为空
                self.left = Node(data)  # 当仁不让的插入
            else:                   # 非空的话
                self.left.insert(data)  # 以左树叉为节点继续插入

        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def search(self, data, parent=None):
        '''
        data为目标查询值，同时返回parent(父节点)便于定位。
        '''
        if data < self.data:
            if self.left is None:
                return None, None
            else:
                return self.left.search(data, self)

        elif data > self.data:
            if self.right is None:
                return None, None

            return self.right.search(data, self)
        else:
          #  return self.data, parent.data
            return self, parent

    def print_tree_in(self):  # 中序
        if self.left:
            self.left.print_tree_in()
        print(self.data)
        if self.right:
            self.right.print_tree_in()

    def print_tree_pre(self):  # 前序
        print(self.data)
        if self.left:
            self.left.print_tree_pre()
        if self.right:
            self.right.print_tree_pre()

    def print_tree_post(self):  # 后序
        if self.left:
            self.left.print_tree_post()
        if self.right:
            self.right.print_tree_post()
        print(self.data)

    def chrildren(self):
        count = 0
        if self.left:
            count += 1

        if self.right:
            count += 1

        return count

    def delete(self, data):
        node, parent = self.search(data)
        chrildren = node.chrildren()  # 子节点数目
        if chrildren == 0:  # 情况 1， 没有子节点，直接删除即可
            if parent.left is node:  # 判断目标节点是其父节点的 左or右 节点
                parent.left = None
            else:
                parent.right = None
            del node

        elif chrildren == 1:  # 情况 2， 有一个子节点，用子节点替换其即可
            if node.left:
                tmp = node.left
            else:
                tmp = node.right
            if parent:
                if parent.left is node:
                    parent.left = tmp
                else:
                    parent.right = tmp
                del node
        else:
            '''
            第三种情况比较复杂：
            1. 左节点0个子节点
            2. 左节点1个子节点
            3. 左节点2个子节点
            '''
            parent = node
            successor = node.right
            while successor.left:  # 递归思想，直至找到最左的子节点， 保持树的平衡，用右子节点的值替换
                parent = successor
                successor = successor.left
                node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

# 接下来可以测试以下种的树怎么样啦。
root = Node(11)
root.insert(14)
root.insert(9)
root.insert(9)
root.insert(7)
root.insert(10)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(8)
value, parent = root.search(10)
print(value.data, parent.data)
root.print_tree_in()
print('*' * 20)
root.delete(4)
root.print_tree_in()
