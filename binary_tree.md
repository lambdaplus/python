---
title: 二叉树
date: 2016-09-23 15:32:24
tags: Algorithm
---
畏惧了好久的二叉树，终于在近两天开搞了。二分法查找已在前几天完成，磨刀霍霍向猪羊，吼吼吼！
何为二叉树？按照我目前的理解就是类似于发叉的树，树干上发两个叉或者一个(不发叉的树真不到有何用处)，发叉的地方称为**节点**。然后发的两个叉又可以继续像树干一样发叉，新发的叉有可以继续发叉，子又生子，孙又生孙，无穷尽也！但是**树的左边的叉的值小于节点值，右边的大于节点值**。

本文参考：
[老齐的Github](https://github.com/qiwsir/algorithm/blob/master/binary_tree.md)

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
转眼间小树苗涨的太旺盛了，疯涨啊！！怎么办呢，剪几个枝吧。别怪我哦，小树苗！
删除节点时，有三种可能的情况：

1. 目标节点下没有任何节点(0个)
2. 目标节点下有一个节点
3. 目标节点下有两个节点

判断节点数目程序如下：
```python
class Node：
    ```
    省略代码
    ```
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
    ```
    省略
    ```

    def delete(self, data):
        node, parent = self.search(data) 
        chrildren = node.chrildren() # 子节点数目
        if chrildren == 0: # 情况 1
            if parent.left is node: # 判断目标节点是其父节点的 左or右 节点
                parent.left = None
            else:
                parent.right = None
            del node

        elif chrildren == 1: # 情况 2
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
        else:                # 情况 3 没看太懂，过两天再看吧
        '''
        第三种情况比较复杂
        1. 左节点0个子节点
        2. 左节点1个子节点
        3. 左节点2个子节点
        '''
            parent = node
            successor = node.left
            while successor.left:
                parent = successor
                successor = successor.left
            node.data = successor.data
            if parent.left = successor:
                parent.left = successor.right
            else:
                parent.left = successor.right


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
root.print_tree()
print('*' * 20)
root.delete(4)
root.print_tree()

```

把自己理解的部分写了写。当做练习，就先当个α版吧。

`2016-05-28`
