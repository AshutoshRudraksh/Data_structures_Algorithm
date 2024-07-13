# parse the input file
def read-input(file_path):
  #we read the file and split each line into components of the object type and its coordinates
  with open(file_path, 'r') as file:
      lines = file.readlines()
  return [line.strip().split() for line in lines]
  
# construct the grid
def construct_grid(objects):
    # build the dictionary that maps each coordinates to its corrsponding objects
    grid = {} 
    #also keeping track of source and sink
    sinks = []
    source = None
    max_x, max_y = 0, 0

    for obj, x, y in objects:
        x, y = int(x), int(y)
        if obj == '*':
            source = (x,y)
        elif obj.isupper():
            sinks.append((x,y, obj))
        if (x,y) not in grid:
            grid[(x,y)] = obj
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return grid, source, sinks, max_x, max_y

# define the pipe connections
def get_neighbors(x,y,pipe):
  # use dictionary to define the possible connections for each type of pipe.
  connections = { 
      '═': [(0,-1),(0,1)],
      '║': [(-1,0),(1,0)],
      '╔'': [(1,0),(0,1)],
      '╗': [(1,0),(0,-1)],
      '╚': [(0,-1),(0,1)],
      '╝': [(-1,0),(0,-1)],
      '╠': [(-1,0),(1,0),(0,1)],
      '╣': [(-1,0),(1,0),(0,-1)],
      '╦': [(1,0),(0,-1),(0,1)],
      '╩': [(-1,0),(0,-1),(0,1)],
  }
  return connections.get(pipe, [(0,1),(0,-1),(1,0),(-1,0)])
  

# perform bfs to determine connectivity
def bfs(source, grid):
    queue = [source]
    visited = set()
    visited.add(source)
    connected_sinks = set()

    while queue:
        x,y = queue.pop(0)
        if grid[(x,y)].isupper():
            connected_sinks.add(grid[(x,y)])

        for dx, dy in get_neighbors(x,y, grid[(x,y)]):
            nx, ny = x+dx, y+dy
            if (nx, ny) in grid and (nx, ny) not in visited:
                if (nx-dx, ny-dy) in grid and (nx, ny) in grid and \
                    (dx,dy) in get_neighbors(nx, ny, grid[(nx,ny)]):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    

    return ''.join(sorted(connected_sinks))

#return result
def find_connected_sinks(file_path):
  #collect all connnected sinks and return them in alphabetical order as a sting

  objects = read_input(file_path):
  grid, source, sinks, max_x, max_y = construct_grid(objects)
  return bfs(source, grid)