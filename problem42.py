'''

As more and more rabbits were rescued from Professor Booleans horrid laboratory, you had to develop a system to track them, since some habitually continue to gnaw on the heads of their brethren and need extra supervision. For obvious reasons, you based your rabbit survivor tracking system on a binary search tree, but all of a sudden that decision has come back to haunt you.
To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily enough, had a distinct age. For a given group, the first rabbit became the root, and then the next one (taken in order of rescue) was added, older ages to the left and younger to the right. The order that the rabbits returned to you determined the end pattern of the tree, and herein lies the problem.
Some rabbits were rescued from multiple cages in a single rescue operation, and you need to make sure that all of the modifications or pathogens introduced by Professor Boolean are contained properly. Since the tree did not preserve the order of rescue, it falls to you to figure out how many different sequences of rabbits could have produced an identical tree to your sample sequence, so you can keep all the rescued rabbits safe.
For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it would result in a binary tree identical to one created from [5, 2, 9, 1, 8].
You must write a function answer(seq) that takes an array of up to 50 integers and returns a string representing the number (in base-10) of sequences that would result in the same tree as the given sequence.

'''



def answer(seq):
    import math
    # Node class: can traverse chlidren, and parents, can add node to the
    # Tree, and each node tracks count of all children below it
    # (descendant_count)

    class Node():

        def __init__(self, value, parent=False):
            self.parent = parent
            self.value = value
            self.small_child = ''
            self.big_child = ''
            self.descendant_count = 1
        # Increase descendant_count of current node and all of its parents

        def add_descendant(self):
            self.descendant_count += 1
            if self.parent:
                self.parent.add_descendant()
        # Add node to Tree

        def add_node(self, value):
            # If current node doesn't have small/big child, add new node. If it
            # does, recursively run add_node on that child
            if value < self.value:
                if not self.small_child:
                    self.small_child = Node(parent=self, value=value)
                    self.add_descendant()
                else:
                    self.small_child.add_node(value)
            else:
                if not self.big_child:
                    self.big_child = Node(parent=self, value=value)
                    self.add_descendant()
                else:
                    self.big_child.add_node(value)
    # Convert seq into a tree structure; return its root

    def make_tree(seq):
        Tree = Node(value=seq[0])
        seq[:1] = []
        for num in seq:
            Tree.add_node(num)
        return Tree
    # Make tree out of inputed sequence
    root = make_tree(seq)
    # Helper: combination function

    def nCr(n, r):
        f = math.factorial
        return f(n) / f(r) / f(n - r)
    # Get total count:

    def get_count(tree):
        if tree == '':
            return 1
        small_count, big_count = 0, 0
        if tree.small_child:
            small_count = tree.small_child.descendant_count
        if tree.big_child:
            big_count = tree.big_child.descendant_count

        return nCr(small_count + big_count, big_count) * \
            get_count(tree.small_child) * \
            get_count(tree.big_child)
    return str(get_count(root))
