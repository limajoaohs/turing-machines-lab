#include <iostream>
#include <vector>
#include <numeric>

void dfs(int u, const std::vector<std::vector<int>>& adj, std::vector<int>& subordinate_count) {
    int count = 0;
    for (int v : adj[u]) {
        dfs(v, adj, subordinate_count);
        count += 1 + subordinate_count[v];
    }
    subordinate_count[u] = count;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    if (n == 1) {
        std::cout << 0 << std::endl;
        return 0;
    }

    std::vector<std::vector<int>> adj(n + 1);
    for (int i = 2; i <= n; ++i) {
        int boss;
        std::cin >> boss;
        adj[boss].push_back(i);
    }

    std::vector<int> subordinate_count(n + 1, 0);
    dfs(1, adj, subordinate_count);

    for (int i = 1; i <= n; ++i) {
        std::cout << subordinate_count[i] << (i == n ? "" : " ");
    }
    std::cout << std::endl;

    return 0;
}