def bfs_search(names):
    queue = names[:]
    
    while queue:
        name = queue.pop(0)  # pop the first element in the queue
        if len(name) == 7:
            return name
    return None

def dfs_search(names):
    stack = names[:]
    
    while stack:
        name = stack.pop()  # pop the last element in the stack
        if len(name) == 7:
            return name
    return None


names = [
    "Michael", "Jessica", "Matthew", "Ashley", "Joshua", "Amanda", "Daniel", "David", 
    "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", 
    "Sarah", "Christopher", "Jennifer", "Lisa", "Nancy", "Karen", "Betty", "Helen"
]

result_bfs = bfs_search(names)
print(f"BFS found a seven-letter name: {result_bfs}")

result_dfs = dfs_search(names)
print(f"DFS found a seven-letter name: {result_dfs}")
