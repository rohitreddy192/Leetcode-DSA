from typing import List

class Trie:
    def __init__(self):
        self.children = {}   # key: dir/file name → Trie node
        self.content = ""    # for files: store text
        self.isFile = False  # True if this node is a file


class FileSystem:

    def __init__(self):
        self.root = Trie()

    def _traverse(self, path: str) -> Trie:
        """Helper: follow the path and return the final Trie node."""
        node = self.root
        if path == "/":  # root case
            return node
        parts = path.split("/")[1:]  # skip first empty from leading "/"
        for part in parts:
            if part not in node.children:
                node.children[part] = Trie()
            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if node.isFile:
            # if path is a file → return just its name
            return [path.split("/")[-1]]
        # else return sorted list of children
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)  # just ensures path nodes exist

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath)
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        return node.content
