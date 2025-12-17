#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

void findPath(int startNode, int n, std::map<int, std::vector<int>>& adj) {
    std::vector<int> path;
    
    int prev = -1; 
    int current = startNode;

    for (int i = 0; i <= n; ++i) {
        path.push_back(current);
        
        for (int neighbor : adj[current]) {
            if (neighbor != prev) {
                prev = current;
                current = neighbor;
                break;
            }
        }
    }
    for (size_t i = 0; i < path.size(); ++i) {
        std::cout << path[i] << (i == path.size() - 1 ? "" : " ");
    }
    std::cout << std::endl;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    std::map<int, std::vector<int>> adj;
    std::map<int, int> degree;

    for (int i = 0; i < n; ++i) {
        int u, v;
        std::cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    int startNode = -1;
    for (auto const& [city, deg] : degree) {
        if (deg == 1) {
            startNode = city;
            break;
        }
    }
    
    findPath(startNode, n, adj);

    return 0;
}