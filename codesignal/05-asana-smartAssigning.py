def smartAssigning(names, statuses, projects, tasks):
    maxTasks = maxProjects = float('inf')
    highest = None
    
    for i in range(len(names)):
        if statuses[i]:
            continue
        if tasks[i] < maxTasks or (tasks[i] == maxTasks and projects[i] < maxProjects):
            maxTasks = tasks[i]
            maxProjects = projects[i]
            highest = names[i]
    
    return highest