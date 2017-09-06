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