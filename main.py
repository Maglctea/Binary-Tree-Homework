from typing import Tuple, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    def __init__(self, root_value: int) -> None:
        self.root = Node(root_value)

    def add(self, value: int) -> None:
        """Функция добавления новой ноды в бинарное дерево. Принимает в себя значение, которое нужно добавить"""
        res = self.search(self.root, value)

        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    def search(self, node: Node, value: int, parent=None) -> Tuple[Optional[Node], Optional[Node]]:
        """Функция поиска значения в данном древе. Принимает в себя ноду, её значени"""
        if node is None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def count(self) -> int:
        """Запуск рекурсивной функции подсчета числа элементов списка"""
        return self.__count_recursive(self.root, 1)

    def __count_recursive(self, node: Node, count: int = 1) -> int:
        """
        Рекурсивная функция подсчета элементов в бинарном дереве. Считает сколько элементов в леаой ветви,
        потом в правой. А после суммирует эти значения.
        Принимает в себя корневой ноды и стартовую точку отсчета числа элементов древа.
        """
        if node is None:
            return 0
        left = self.__count_recursive(node.left, count + 1)
        right = self.__count_recursive(node.right, count + 1)

        return 1 + left + right

    def print_tree(self) -> None:
        """Запускает рекурсивную функцию печати в консоль форматированного вывода бинарного дерева"""
        self.__print_tree_recursive(self.root, '')

    def __print_tree_recursive(self, node: Node, indent: str) -> None:
        """Рекурсивная функция печати в консоль форматированного вывода дерева.
        Принимает в себя родительскую ноду и отступ от начала строкаи"""
        if node is None:
            return

        if indent == '':
            print(f"    {node}")

        else:
            print(f"{indent}└── {node.value}")
        indent = indent + "    "

        self.__print_tree_recursive(node.left, indent + "|")
        self.__print_tree_recursive(node.right, indent)

    def delete(self, value: int) -> None:
        """Запускает функцию удаления элемента из бинарного дерева. Принимает в себя значение.ю которое нужно удалить"""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node: Node, value: int) -> Optional[Node]:
        """
        Рекурсивная функция для удаления элемента из бинарного дерева.
        Изначально принимает в себя родительскую ноду и значение, которое надо удалить.
        """
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Случай 1: Нет дочерних узлов или только один дочерний узел
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Случай 2: Два дочерних узла
            successor = self.__find_min(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        return node

    def __find_min(self, node: Node) -> Node:
        """Передаем ноду и получаем крайний минимальный элемент"""
        current = node
        while current.left is not None:
            current = current.left
        return current


bt = BinaryTree(5)
bt.add(10)
bt.add(9)
bt.add(14)
bt.add(11)
bt.add(15)
bt.add(3)

print(f'Кол-во элементов до удаления: {bt.count()}')
bt.print_tree()
bt.delete(10)
bt.print_tree()
print(f'Кол-во элементов после удаления: {bt.count()}')
