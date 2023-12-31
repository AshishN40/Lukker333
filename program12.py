Q12)Implement a system that performs arrangement of some set of objects in a room. Assume that you have only 5 rectangular, 4 square-shaped objects. Use A* approach for the placement of the objects in room for efficient space utilisation. Assume suitable heuristic, and dimensions of objects and rooms. (Informed Search)
# Define a class for objects with attributes (name, width, height)
class Object:
    def _init_(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

# Define the room dimensions (width, height)
room_width = 10
room_height = 10

# Define a list of objects to be placed
objects = [
    Object("Rect1", 2, 4),
    Object("Rect2", 3, 2),
    Object("Rect3", 1, 5),
    Object("Rect4", 3, 3),
    Object("Square1", 2, 2),
]

# Define a heuristic function to maximize space utilization
def heuristic(state, remaining_objects):
    empty_space = room_width * room_height
    for obj in remaining_objects:
        if obj.width <= room_width - state[0] and obj.height <= room_height - state[1]:
            empty_space -= obj.width * obj.height
    return empty_space

# Define A* search function
def astar_search(room_width, room_height, objects):
    initial_state = (0, 0)
    remaining_objects = list(objects)
    state_stack = [(0, initial_state, remaining_objects, [])]

    while state_stack:
        cost, state, remaining_objects, path = state_stack.pop()
        if not remaining_objects:
            return path  # Return the placement path

        for obj in remaining_objects:
            for x in range(room_width):
                for y in range(room_height):
                    new_state = (x, y)
                    if (
                        x + obj.width <= room_width
                        and y + obj.height <= room_height
                    ):
                        new_cost = cost + heuristic(new_state, remaining_objects)
                        new_remaining_objects = [o for o in remaining_objects if o != obj]
                        new_path = path + [(obj.name, new_state)]
                        state_stack.append((new_cost, new_state, new_remaining_objects, new_path))

    return None

# Perform A* search to arrange objects
placement_path = astar_search(room_width, room_height, objects)

if placement_path:
    print("Object Placement:")
    for obj_name, (x, y) in placement_path:
        print(f"{obj_name}: ({x}, {y})")
else:
    print("No valid arrangement found.")
