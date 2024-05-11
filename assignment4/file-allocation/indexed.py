class IndexedAllocation:
    def __init__(self, size):
        self.disk = [None] * size
        self.index = {}

    def create_file(self, name, size):
        blocks = []
        for i in range(len(self.disk)):
            if self.disk[i] is None:
                blocks.append(i)
                if len(blocks) == size:
                    self.index[name] = blocks
                    for block in blocks:
                        self.disk[block] = name
                    return
        print("Not enough space")

    def delete_file(self, name):
        if name in self.index:
            for block in self.index[name]:
                self.disk[block] = None
            del self.index[name]

    def list_files(self):
        for file in self.index:
            print(file)

allocation = IndexedAllocation(10)
allocation.create_file("file1", 3)
allocation.create_file("file2", 2)
allocation.list_files()
allocation.delete_file("file1")
allocation.list_files()

# We use a list to represent the disk, where each element represents a block.
# We use a dictionary to represent the index, where the keys are the file names and the values are lists of block numbers.
# The create_file function allocates a list of blocks for a file and updates the index.
# The delete_file function deallocates the space occupied by a file and updates the index.
# The list_files function prints all the files on the disk.