import MPT
import graphviz
from Node import Node

storage = {}

# 1. init() 构造树
mpt = MPT.MerklePatriciaTrie(storage)  

# 2. update() 添加节点
mpt.update(b'b', b'alphabet')
mpt.update(b'bird', b'animal')
mpt.update(b'boy', b'man')
mpt.update(b'boat', b'ship')
mpt.update(b'girl', b'woman')

# 3. get() 查询节点
print('boat:    ', mpt.get(b'boat'))

# 4. update() 更新节点
mpt.update(b'boat', b'Ship')

# 5. get() 查询节点
print('new boat:    ', mpt.get(b'boat'))

# 6. root() 返回根节点
root1 = mpt.root()

# 7. root_hash() 返回根节点的哈希值
root1hash = mpt.root_hash()

# 8. delete() 删除节点
mpt.delete(b'boy')

print("Root hash is     {}".format(root1hash.hex()))
print("New root hash is {}".format(mpt.root_hash().hex()))

# 9. init() 从旧mpt的根节点提取旧mpt 
mpt1 = MPT.MerklePatriciaTrie(storage, root=root1)

print('in old mpt, boy:    ', mpt1.get(b'boy'))
print('in newest mpt, boy: ', end='')
try:
    print(mpt.get(b'boy'))
except KeyError:
    pass

# print(len(storage))
# for key, value in storage.items():
#     print(format(key.hex()), format(value.hex()))


def draw_mpt_tree(mpt):
    dot = graphviz.Digraph()
    _add_node(dot, mpt.root(), mpt._storage)
    dot.format = 'png'  # 设置输出格式为PNG，可根据需要修改

    dot.render('mpt_tree')  # 保存为文件，可根据需要修改文件名


def _add_node(dot, node_ref, storage):
    node = mpt._get_node(node_ref)
    node_label = str(node)
    dot.node(node_ref, label=node_label)

    if isinstance(node, Node.Branch):
        for idx, branch_ref in enumerate(node.branches):
            if branch_ref:
                dot.edge(node_ref, branch_ref, label=str(idx))
                _add_node(dot, branch_ref, storage)
    elif isinstance(node, (Node.Extension, Node.Leaf)):
        if node.next_ref:
            dot.edge(node_ref, node.next_ref)
            _add_node(dot, node.next_ref, storage)


draw_mpt_tree(mpt)