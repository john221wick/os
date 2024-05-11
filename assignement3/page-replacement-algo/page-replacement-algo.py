# FIFO (First-In-First-Out) Algorithm:
# Iterate over the pages.
# If a page is not in the frames, add it to the frames and increment the page fault count.
# If the frames are full, remove the first page from the frames.
# If a page is already in the frames, move it to the end of the frames.

# LRU (Least Recently Used) Algorithm:
# Iterate over the pages.
# If a page is not in the frames, add it to the frames and increment the page fault count.
# If the frames are full, remove the least recently used page from the frames.
# If a page is already in the frames, move it to the end of the frames.

# LFU (Least Frequently Used) Algorithm:
# Iterate over the pages.
# If a page is not in the frames, add it to the frames and increment the page fault count.
# If the frames are full, remove the least frequently used page from the frames.
# If a page is already in the frames, increment its frequency count.

def FIFO(pages, capacity):
    page_faults = 0
    frames = []
    for page in pages:
        if page not in frames:
            if len(frames) == capacity:
                frames.pop(0)
            frames.append(page)
            page_faults += 1
        else:
            frames.remove(page)
            frames.append(page)
    print("Page Faults:", page_faults)

def LRU(pages, capacity):
    page_faults = 0
    frames = []
    for page in pages:
        if page not in frames:
            if len(frames) == capacity:
                lru_page = min(frames, key=pages.index)
                frames.remove(lru_page)
            frames.append(page)
            page_faults += 1
        else:
            frames.remove(page)
            frames.append(page)
    print("Page Faults:", page_faults)

def LFU(pages, capacity):
    page_faults = 0
    frames = []
    page_count = {}
    for page in pages:
        if page not in frames:
            if len(frames) == capacity:
                lfu_page = min(frames, key=lambda x: page_count[x])
                frames.remove(lfu_page)
                del page_count[lfu_page]
            frames.append(page)
            page_count[page] = 1
            page_faults += 1
        else:
            page_count[page] += 1
    print("Page Faults:", page_faults)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3

print("FIFO:")
FIFO(pages, capacity)
print("\nLRU:")
LRU(pages, capacity)
print("\nLFU:")
LFU(pages, capacity)