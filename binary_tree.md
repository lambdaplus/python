---
更新 `2017-03-22`
---

畏惧了好久的二叉树，终于在近两天开搞了。二分法查找已在前几天完成，磨刀霍霍向猪羊，吼吼吼！ 何为二叉树？按照我目前的理解就是类似于发叉的树，树干上发两个叉或者一个(不发叉的树真不到有何用处)，发叉的地方称为**节点**。然后发的两个叉又可以继续像树干一样发叉，新发的叉有可以继续发叉，子又生子，孙又生孙，无穷尽也！但是**树的左边的叉的值小于节点值，右边的大于节点值**。

本文参考： [老齐的Github](https://github.com/qiwsir/algorithm/blob/master/binary_tree.md)

首先，建立一棵树。

```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
```

这样，光秃秃的小树苗就种好了。接着就是茁长生长啦。浇水去喽！

```python
class Node：
    '''
    ...
    '''
    def insert(self, data):
        if data < self.data: # 树叉小于节点
            if self.left is None: # 并且左面的树叉为空
                self.left = Node(data) # 当仁不让的插入
            else:                   # 非空的话
                self.left.insert(data) # 以左树叉为节点继续插入

        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
```

浇完水后，小树苗噌噌的往上窜啊。

```python
class Node：
    '''
    省略上述代码
    '''
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
```

树苗生长的那么好，想看看每个叉上都是啥呀，来来来，抬头往上看((其实是往下看啦)。

```python
def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
```

树的遍历又分为以下三种：

1. 前序(root -> left -> right)
2. 中序(left -> root -> right)
3. 后序(left -> right -> root)

调整`print_tree`函数里 `print(self.data)` 的顺序即可实现三种遍历方式。

转眼间小树苗涨的太旺盛了，疯涨啊！！怎么办呢，剪几个枝吧。别怪我哦，小树苗！ 删除节点时，有三种可能的情况：

1. 目标节点下没有任何节点(0个)
2. 目标节点下有一个节点
3. 目标节点下有两个节点

判断节点数目程序如下：

```python
class Node：
'''
省略代码
'''
def chrildren(self):
    count = 0
    if self.left:
        count += 1

    if self.right:
        count += 1

    return count
```

接下来就是删除操作啦。哦吼吼。

```python
class Node：
'''
省略
'''

def delete(self, data):
    node, parent = self.search(data)
    chrildren = node.chrildren() # 子节点数目
    if chrildren == 0: # 情况 1， 没有子节点，直接删除即可
        if parent.left is node: # 判断目标节点是其父节点的 左or右 节点
            parent.left = None
        else:
            parent.right = None
        del node

    elif chrildren == 1: # 情况 2， 有一个子节点，用子节点替换其即可
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
    1\. 左节点0个子节点
    2\. 左节点1个子节点
    3\. 左节点2个子节点
    '''
        parent = node
        successor = node.right
        while successor.left:  # 递归思想，直至找到'最左'的子节点， 保持树的平衡，用右子节点的值替换
            parent = successor
            successor = successor.left
        node.data = successor.data
        if parent.left ==  successor:
            parent.left = successor.right
        else:
            parent.right = successor.right

# 接下来可以测试以下种的树怎么样啦。

root = Node(11) root.insert(14) root.insert(9) root.insert(9) root.insert(7) root.insert(10) root.insert(4) root.insert(5) root.insert(6) root.insert(8) value, parent = root.search(10) print(value.data, parent.data) root.print_tree() print('_'_ 20) root.delete(4) root.print_tree()

```
把自己理解的部分写了写。当做练习，就先当个α版吧。
`2016-05-28`


基本搞明白了
完整代码[在这里](https://github.com/lambdaplus/python/blob/master/binary_tree.py)

### 广度遍历和深度遍历二叉树！

```python
def lookup(root):
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)


def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)
    print(root.data)
```
### 求最大树深

```python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
```

### 比较两棵树是否相同

```python
def is_same(t1, t2):
    if t1 == None and t2 == None:
        return True
    elif t1 and t2:
        return t1.data == t2.data and is_same(t1.left, t2.left)\
                                  and is_same(t1.right, t2.right)
    else:
        return False
```

### 已知前序中序求后序

前面说到：
前序: root -> left -> right
中序: left -> root -> right
后序: left -> right -> root

前序: 第一个值 A 即为根节点
中序: A 的左边全为左子树，右边全是右子树

```python
def pre_in_post(pre_order, in_order):
    if not pre_order:
        return
    post = Node(pre_order[0])
    index = in_order.index(pre_order[0])
    post.left = pre_in_post(pre_order[1:index+1], in_order[:index])
    post.right = pre_in_post(pre_order[index+1:], in_order[index+1:])
    return post
```
### 已知前序中序构造出树
```python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return
        tree = TreeNode(pre[0])
        index = tin.index(pre[0])
        tree.left = self.reConstructBinaryTree(pre[1:index+1],tin[:index])
        tree.right = self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
        return tree

    @classmethod
    def print_tree(cls, tree):
        if tree:
            cls.print_tree(tree.left)
            cls.print_tree(tree.right)
            print(tree.val)

pre = [1,2,3,4,5,6,7]
tin = [3,2,4,1,6,5,7]
s = Solution()
t = s.reConstructBinaryTree(pre, tin)
s.print_tree(t)
```
### 树的子结构

```python
求pRoot2 的子树是否为 pRoot2
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def is_subtree(self, t1, t2): 
        if not t2:               # t2 is None 其为子树
            return True
        if not t1:
            return False
        if not t1.val == t2.val:
            return False
        return self.is_subtree(t1.left, t2.left) and self.is_subtree(t1.right, t2.right)
        
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
        	if pRoot1.val == pRoot2.val:
        	    result = self.is_subtree(pRoot1, pRoot2)
        	if not result:
        	    result = self.is_subtree(pRoot1.left, pRoot2)
        	if not result:
        	    result = self.is_subtree(pRoot1.right, pRoot2)
		return result
```
### 对称二叉树

```
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def isSymmetrical(self, pRoot):
        def is_same(p1, p2):
            if not (p1 or p2):
                return True
            elif p1 and p2 and p1.val == p2.val:
                return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
            return False

        if not pRoot:
            return True
        return is_same(pRoot.left, pRoot.right)
```
### 二叉树镜像

```
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        elif not (root.left or root.right):
            return root
    	
        root.left, root.right = root.right, root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
``` 
