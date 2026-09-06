from stack_using_linkedlist import Stack


class solution:

    def stackundoredo(self, data, operations):

        s = Stack()
        undo = Stack()

        # Put original string into stack
        for i in data:
            s.push(i)

        # Perform operations
        for i in operations:

            if i == "u":
                if not s.isEmpty():
                    undo.push(s.pop())

            elif i == "r":
                if not undo.isEmpty():
                    s.push(undo.pop())

        # Convert stack into normal string
        result = []

        while not s.isEmpty():
            result.append(s.pop())

        result.reverse()

        return "".join(result)


data = input("Enter the string to be processed: ")
operations = input("Enter the string of operations: ")

obj = solution()

result = obj.stackundoredo(data, operations)

print("Final string:", result)