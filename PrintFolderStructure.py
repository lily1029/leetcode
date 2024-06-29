class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

class Tree:
    def __init__(self):
        self.root = Node("")
    
    def insert_file(self, file_path):
        folders = file_path.split("/")[1:]  # Exclude the empty root folder

        current = self.root
        for folder in folders:
            if folder not in current.children:
                current.children[folder] = Node(folder)
            current = current.children[folder]

    def print_files(self):
        self._dfs_print(self.root, "")
    
    def _dfs_print(self, node, indent):
        if not node.children:
            print(indent + "-- " + node.name)
            return
    
        print(indent + "-- " + node.name)
        for child in node.children.values():
             self._dfs_print(child, indent + "  ")
if __name__ == '__main__':
    files = [
        "/webapp/assets/html/a.html",
        "/webapp/assets/html/b.html",
        "/webapp/assets/js/c.js",
        "/webapp/index.html"
    ]

    tree = Tree()
    for file in files:
        tree.insert_file(file)

    tree.print_files()
    

        
        