class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def createBST(self, l):
        """
        Time Complexity: O(n*log(n))
        Space_Complexity: O(1)
        """
        # check if the list is empty
        if len(l) < 1:
            return ""
        for ele in l:
            # check if there is a root
            if not self.root:
                self.root = Node(ele)
            # if the root exists, insert every element
            else:
                self.__insert_ele(self.root, ele)
        return self.inOrderTraversal()

    # private helper method to insert the elements in their right position
    def __insert_ele(self, start, val):
        if start.value < val:
            if start.right:
                self.__insert_ele(start.right, val)
            else:
                start.right = Node(val)
        elif start.value > val:
            if start.left:
                self.__insert_ele(start.left, val)
            else:
                start.left = Node(val)

    def search(self, val):
        """
        Time Complexity: O(log(n))
        Space_Complexity: O(1)
        """
        start = self.root
        while start:
            if start.value == val:
                return True
            elif start.value > val:
                start = start.left
            else:
                start = start.right
        return False

    def inOrderTraversal(self):
        """
        Time Complexity: O(n)
        Space_Complexity: O(1)
        """
        traverse = ""
        return self.__inOrderTraversal(self.root, traverse)[:-1]

    def __inOrderTraversal(self, root, traverse):
        if root:
            traverse = self.__inOrderTraversal(root.left, traverse)
            traverse += str(root.value) + "-"
            traverse = self.__inOrderTraversal(root.right, traverse)
        return traverse

