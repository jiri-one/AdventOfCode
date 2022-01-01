# result of test_input1.txt file have to be 36
# result of test_input2.txt file have to be 103
# result of test_input3.txt file have to be 3509
# result of input.txt file have to be 149220

caves_with_ep= dict()
caves_in_list = list()
all_caves_in_set = set()

with open("input.txt", "r") as file:
    while line:=file.readline().strip():
        caves_in_list.append(line.split("-"))
        all_caves_in_set.add(line.split("-")[0])
        all_caves_in_set.add(line.split("-")[1])


# create caves with all entry points
for cave in all_caves_in_set:
    caves_with_ep[cave] = set() # it is better to have set here, bacause of duplicity
    for cave_in_pair in list(caves_in_list):
        if cave in cave_in_pair:
            index = cave_in_pair.index(cave)
            if index == 0:
                index = 1
            elif index == 1:
                index = 0
            caves_with_ep[cave].add(cave_in_pair[index])
    caves_with_ep[cave] = list(caves_with_ep[cave]) # but at the end is better to conver set to list, because with list is better work
    #if "end" in caves_with_ep[cave]: # end have to be last in list
        #caves_with_ep[cave].remove("end")
        #caves_with_ep[cave].append("end")


# initial lines with start paths
pending_paths = []
done_paths = []
for value in caves_with_ep["start"]:
    pending_paths.append(["start", value])
    caves_with_ep[value].remove("start")

def others_twice(path, task):
    for cave in task:
        if cave.isupper() == False and task.count(cave) == 2 and cave != path:
            return True
    else:
        return False

# main iteration and combine paths from the maze
while pending_paths:
    task = pending_paths.pop()
    last_cave = task[-1]
    paths_from_last_cave = caves_with_ep[last_cave]
    for path in paths_from_last_cave:
        if path == "end":
            task_copy = task.copy()
            task_copy.append(path)
            done_paths.append(task_copy)
        else:
            if path.isupper() == False and task.count(path) == 2:
                pass
            elif path.isupper() == False and others_twice(path, task) and task.count(path) == 1:
                pass
            else:
                task_copy = task.copy()
                task_copy.append(path)
                pending_paths.append(task_copy)

print(len(done_paths))



