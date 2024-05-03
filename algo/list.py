class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
    
class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: any) -> None:
        """リストの末尾にノードを追加"""
        new_node = Node(data)
        # そもそもリストが空の場合
        if self.head is None:
            self.head = new_node
            return
        
        # リストが空でない場合
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data: any) -> None:
        """リストの先頭にノードを追加"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        """リスト内の全てのノードを表示"""
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def remove(self, data: any) -> None:
        """指定されたデータを持つノードを削除"""
        cur_node = self.head
        # ノードが先頭にある場合
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return
    
        # ノードが先頭以外にある場合
        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        # ノードが見つからなかった場合
        if cur_node is None:
            return
        
        # ノードが見つかった場合
        prev.next = cur_node.next
        cur_node = None


if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.prepend(0)
    
    l.print()

    l.remove(3)