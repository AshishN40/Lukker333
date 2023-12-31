#Q7)Write a program to implement Water Jug Problem
def water_jug_problem(jug1_capacity, jug2_capacity, target):
    jug1 = 0
    jug2 = 0
    steps = []

    def is_goal_state(jug1, jug2, target):
        return jug1 == target or jug2 == target

    def fill_jug1():
        nonlocal jug1
        jug1 = jug1_capacity
        steps.append(f"Fill jug1 ({jug1}L)")

    def fill_jug2():
        nonlocal jug2
        jug2 = jug2_capacity
        steps.append(f"Fill jug2 ({jug2}L)")

    def empty_jug1():
        nonlocal jug1
        jug1 = 0
        steps.append(f"Empty jug1 (0L)")

    def empty_jug2():
        nonlocal jug2
        jug2 = 0
        steps.append(f"Empty jug2 (0L)")

    def pour_jug1_to_jug2():
        nonlocal jug1, jug2
        space_in_jug2 = jug2_capacity - jug2
        if jug1 <= space_in_jug2:
            jug2 += jug1
            jug1 = 0
        else:
            jug1 -= space_in_jug2
            jug2 = jug2_capacity
        steps.append(f"Pour from jug1 to jug2 ({jug1}L -> {jug2}L)")

    def pour_jug2_to_jug1():
        nonlocal jug1, jug2
        space_in_jug1 = jug1_capacity - jug1
        if jug2 <= space_in_jug1:
            jug1 += jug2
            jug2 = 0
        else:
            jug2 -= space_in_jug1
            jug1 = jug1_capacity
        steps.append(f"Pour from jug2 to jug1 ({jug2}L -> {jug1}L)")

    while not is_goal_state(jug1, jug2, target):
        if jug1 == 0:
            fill_jug1()
        elif jug1 > 0 and jug2 < jug2_capacity:
            pour_jug1_to_jug2()
        elif jug1 > 0:
            empty_jug2()

    steps.append(f"Goal reached: {target}L in jug1")

    for step in steps:
        print(step)

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_problem(jug1_capacity, jug2_capacity, target)
