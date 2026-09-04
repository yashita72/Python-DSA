class BloomFilter:
    def __init__(self, size=24):
        self.size = size
        self.bit_array = [0] * size

    # ---- Custom Hash Functions ----
    def hash1(self, item):
        h = 0
        for ch in str(item):
            h = (h * 31 + ord(ch)) % self.size
        return h

    def hash2(self, item):
        h = 0
        for ch in str(item):
            h = (h * 37 + ord(ch) * 3) % self.size
        return h

    def hash3(self, item):
        h = 0
        for ch in str(item):
            h = (h + ord(ch) * 7) % self.size
        return h

    def get_hash_indices(self, item):
        return [self.hash1(item), self.hash2(item), self.hash3(item)]

    # ---- Add element ----
    def add(self, item):
        for idx in self.get_hash_indices(item):
            self.bit_array[idx] = 1
        print(f"Added '{item}' -> indices {self.get_hash_indices(item)}")

    # ---- Check element ----
    def check(self, item):
        indices = self.get_hash_indices(item)
        present = all(self.bit_array[idx] == 1 for idx in indices)
        if present:
            print(f"'{item}' MAY be present -> indices {indices}")
        else:
            print(f"'{item}' is DEFINITELY NOT present -> indices {indices}")
        return present

    def show_filter(self):
        print("Bit Array:", self.bit_array)


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    bf = BloomFilter(size=24)

    # Add elements
    elements_to_add = ["apple", "banana", "grape", "mango"]
    for e in elements_to_add:
        bf.add(e)

    bf.show_filter()
    print()

    # Check elements (some present, some not)
    elements_to_check = ["apple", "banana", "orange", "kiwi", "grape"]
    for e in elements_to_check:
        bf.check(e)