from collections import deque

# Hamara graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

def bfs(graph, start_node):
    visited = set()       # Track rakhne ke liye ki kaunsa node visit ho chuka hai
    queue = deque([start_node]) # Queue mein starting node daal diya
    
    visited.add(start_node)
    
    while queue:
        current_node = queue.popleft() # Queue ke aage se node nikala
        print(current_node, end=" ")   
        print("Current node:", current_node)
        
        # Iske saare neighbors check karo
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Queue ke pichhe daal diya

# Function call kiya 'A' se start karke
bfs(graph, 'B')