import matplotlib.pyplot as plt


def plot_mpt_tree(tree, node_name=None, parent=None):
    if parent is None:
        plt.figure(figsize=(6, 6))
        plt.title('MPT Tree')
    if node_name:
        plt.text(tree[node_name]['x'], tree[node_name]['y'], node_name,
                 ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    children = tree[node_name]['children']
    for child in children:
        child_node = tree[child]
        plt.plot([tree[node_name]['x'], child_node['x']],
                 [tree[node_name]['y'], child_node['y']], '-k')

        plot_mpt_tree(tree, child, node_name)


def draw_mpt_tree(tree):
    first_key = next(iter(mpt_tree))
    plot_mpt_tree(tree, first_key)
    plt.axis('off')
    plt.show()


# 示例MPT数据
mpt_tree = {
    'A': {'x': 0, 'y': 0, 'children': ['B', 'C']},
    'B': {'x': -1, 'y': -1, 'children': ['D', 'E']},
    'C': {'x': 1, 'y': -1, 'children': ['F', 'G']},
    'D': {'x': -2, 'y': -2, 'children': []},
    'E': {'x': 0, 'y': -2, 'children': []},
    'F': {'x': 0, 'y': -2, 'children': []},
    'G': {'x': 2, 'y': -2, 'children': []}
}

draw_mpt_tree(mpt_tree)
