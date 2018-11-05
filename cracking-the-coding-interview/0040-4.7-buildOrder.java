// Topological sort
public Deque<Vertex<T>> topologicalSort(Graph<T> graph) {
    Deque<Vertex<T>> stack = new LinkedList<>();
    Set<Vertex<T>> visited = new HashSet<>();

    for (Vertex<T> vertex : graph.getAllVertex()) {
        if (!visited.contains(vertex)) topologicalSort(vertex, stack, visited);
    }

    return stack;
}

private void topologicalSort(Vertex<T> vertex, Deque<Vertex<T>> stack, Set<Vertex<T>> visited) {
    visited.add(vertex);
    for (Vertex<T> child : vertex.getAdjacentVertexes()) {
        if (!visited.contains(child)) topologicalSort(child, stack, visited);
    }
    stack.push(vertex);
}

// CTCI: Solution 2 - topological sort - DFS
Deque<Project> findBuildOrder(String[] projects, String[][] dependencies) {
    Graph graph = buildGraph(projects, dependencies);
    return orderProjects(graph.getProjects());
}

Deque<Project> orderProjects(List<Project> projects) {
    Deque<Project> stack = new LinkedList<>();
    Set<Project> visited = new HashSet<>();
    Set<Project> visiting = new HashSet<>();

    for (Project project : projects) {
        if (!visited.contains(project)) visit(project, stack, visited, visiting);
    }

    return stack;
}

void visit(Project project, Deque<Project> stack, Set<Project> visited, Set<Project> visiting) {
    if (visiting.contains(project)) throw new RuntimeException("Graph is not acyclic");
    if (!visited.contains(project)) {
        visiting.add(project);
        for (Project child: project.getChildren) visit(child, stack, visited, visiting);
        visiting.remove(project);
        visited.add(project);
        stack.push(project);
    }
}

// CTCI: Solution 1
public class Project {
    private List<Project> children = new ArrayList<>();
    private Map<String, Project> map = new HashMap<>();
    private String name;
    private int dependencies = 0;

    public Project(String name) { this.name = name; }

    public addNeighbor(Project project) {
        if (!map.contains(project.getName())) {
            children.add(project);
            map.put(project.getName(), project);
            project.incrementDependencies();
        }
    }

    public void incrementDependencies() { this.dependencies++; }
    public void decrementDependencies() { this.dependencies--; }

    public String getName() { return name; }
    public List<Project> getChildren() { return children; }
    public int getDependencies() { return dependencies; }
}

public class Graph {
    private List<Project> projects = new ArrayList<>();
    private Map<String, Project> map = new HashMap<>();

    public void createProject(String name) {
        if (!map.contains(name)) {
            Project project = new Project(name);
            projects.add(project);
            map.put(name, project);
        }
    }

    public Project getProject(String name) { return map.get(name); }

    public void addEdge(String startName, String endName) {
        Project start = getProject(startName);
        Project end = getProject(endName);
        start.addNeighbor(end);
    }

    public List<Project> getProjects() { return projects; }
}

Project[] findBuildOrder(String[] projects, String[][] dependencies) {
    Graph graph = buildGraph(projects, dependencies);
    return orderProjects(graph.getProjects());
}

Graph buildGraph(String[] projects, String[][] dependencies) {
    Graph graph = new Graph();

    for (String project : projects) graph.createProject(project);

    for (String[] dependency : dependencies) {
        String first = dependency[0];
        String second = dependency[1];
        graph.addEdge(first, second);
    }

    return graph;
}

Project[] orderProjects(List<Project> projects) {
    Project[] buildOrder = new Project[projects.size()];

    int endOfList = addNonDependent(buildOrder, projects, 0);

    int toBeProcessed = 0;
    while (toBeProcessed < buildOrder.length) {
        Project current = buildOrder[toBeProcessed];

        if (current == null) return null;

        List<Project> children = current.getChildren();
        for (Project child : children) { child.decrementDependencies(); }

        endOfList = addNonDependent(buildOrder, projects, endOfList);
        toBeProcessed++;
    }

    return buildOrder;
}

int addNonDependent(Project[] buildOrder, List<Project> projects, int endOfList) {
    for (Project project : projects) {
        if (project.getDependencies() == 0) {
            buildOrder[endOfList++] = project; 
        }
    }

    return endOfList;
}