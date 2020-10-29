left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, 1)

width = 5
height = 5

start_x = 0 # y = 0 ofc
end_x = 0 # y = height ofc

arr = [[0 for x in range(width)] for y in range(height)]
visited = [[False for x in range(width)] for y in range(height)]

arr[start_y][start_x] = 1
visited[start_y][start_x] = True

states = []

class State:
    def __init__(_arr, _visited):
        self.arr = _arr
        self.visited = _visited

while True:
    current_arr = arr_stack.pop()
    current_visited = visited_.pop()