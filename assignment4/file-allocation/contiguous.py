class ContiguousAllocation:
    def __init__(self, size):
        self.disk = [None] * size

    def create_file(self, name, size):
        for i in range(len(self.disk)):
            if self.disk[i] is None:
                if i + size <= len(self.disk):
                    for j in range(i, i + size):
                        self.disk[j] = name
                    return
        print("Not enough space")

    def delete_file(self, name):
        for i in range(len(self.disk)):
            if self.disk[i] == name:
                self.disk[i] = None

    def list_files(self):
        files = set()
        for block in self.disk:
            if block is not None:
                files.add(block)
        for file in files:
            print(file)

allocation = ContiguousAllocation(10)
allocation.create_file("file1", 3)
allocation.create_file("file2", 2)
allocation.list_files()
allocation.delete_file("file1")
allocation.list_files()

# We use a list to represent the disk, where each element represents a block.
# The create_file function allocates a contiguous block of space for a file.
# The delete_file function deallocates the space occupied by a file.
# The list_files function prints all the files on the disk.