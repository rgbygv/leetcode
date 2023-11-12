class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root:
                root[ch] = dict()
            root = root[ch]
        root["#"] = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch not in root:
                return False
            root = root[ch]
        return "#" in root

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch not in root:
                return False
            root = root[ch]
        return True
