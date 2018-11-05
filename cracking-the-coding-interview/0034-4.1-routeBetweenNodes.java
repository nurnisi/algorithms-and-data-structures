enum State {
    Unvisited,
    Visited;
}

boolean search(Graph graph, Node start, Node end) {
    if (start == end) return true;

    //mark nodes as unvisited
    for (Node node : graph.getNodes()) node.state = State.Unvisited;

    Queue<Node> queue = new LinkedList<>();
    start.state = State.Visited;
    queue.add(start);

    while (!queue.isEmpty()) {
        Node node = queue.remove();
        for (Node adj : node.getAdjacent()) {
            if (adj == end) return true;
            else if (adj.state == State.Unvisited) {
                adj.state = State.Visited;
                queue.add(adj);
            }
        }
    }
    return false;
}