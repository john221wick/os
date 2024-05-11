class LinkedAllocation:
    def __init__(self, size):
        self.disk = [None] * size
        self.index = {}

    def create_file(self, name, size):
        blocks = []
        for i in range(len(self.disk)):
            if self.disk[i] is None:
                blocks.append(i)
                if len(blocks) == size:
                    self.index[name] = blocks[0]
                    for i in range(len(blocks) - 1):
                        self.disk[blocks[i]] = blocks[i + 1]
                    self.disk[blocks[-1]] = -1
                    return
        print("Not enough space")

    def delete_file(self, name):
        if name in self.index:
            block = self.index[name]
            while block != -1:
                next_block = self.disk[block]
                self.disk[block] = None
                block = next_block
            del self.index[name]

    def list_files(self):
        for file in self.index:
            print(file)

allocation = LinkedAllocation(10)
allocation.create_file("file1", 3)
allocation.create_file("file2", 2)
allocation.list_files()
allocation.delete_file("file1")
allocation.list_files()

# We use a list to represent the disk, where each element represents a block.
# We use a dictionary to represent the index, where the keys are the file names and the values are the block numbers of the first blocks of the files.
# The create_file function allocates a linked list of blocks for a file and updates the index.
# The delete_file function deallocates the space occupied by a file and updates the index.
# The list_files function prints all the files on the disk.