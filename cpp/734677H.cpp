#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    if (n == 1) {
        int val;
        std::cin >> val;
        if (val == 1) {
            std::cout << "Yes\n";
        } else {
            std::cout << "No\n";
        }
        return 0;
    }

    std::vector<std::vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        std::cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    if (a[0] != 1) {
        std::cout << "No\n";
        return 0;
    }

    std::queue<int> q;
    q.push(1);
    std::vector<bool> visited(n + 1, false);
    visited[1] = true;
    int pos = 1;

    bool possible = true;
    while (!q.empty()) {
        int parent = q.front();
        q.pop();

        std::vector<int> children_from_graph;
        for (int neighbor : adj[parent]) {
            if (!visited[neighbor]) {
                children_from_graph.push_back(neighbor);
            }
        }

        int num_children = children_from_graph.size();
        if (pos + num_children > n) {
            possible = false;
            break;
        }

        std::vector<int> children_from_sequence;
        for (int i = 0; i < num_children; ++i) {
            children_from_sequence.push_back(a[pos + i]);
        }

        std::sort(children_from_graph.begin(), children_from_graph.end());
        std::sort(children_from_sequence.begin(), children_from_sequence.end());

        if (children_from_graph != children_from_sequence) {
            possible = false;
            break;
        }

        for (int child : children_from_sequence) {
            visited[child] = true;
            q.push(child);
        }

        pos += num_children;
    }

    if (possible) {
        std::cout << "Yes\n";
    } else {
        std::cout << "No\n";
    }

    return 0;
}