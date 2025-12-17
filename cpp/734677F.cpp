#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, m, k;
vector<string> grid;
vector<vector<bool>> visited;
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

void dfs(int r, int c) {
    if (r < 0 || r >= n || c < 0 || c >= m || grid[r][c] == '#' || visited[r][c]) {
        return;
    }

    visited[r][c] = true;

    for (int i = 0; i < 4; ++i) {
        dfs(r + dr[i], c + dc[i]);
    }

    if (k > 0) {
        grid[r][c] = 'X';
        k--;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;

    grid.resize(n);
    visited.assign(n, vector<bool>(m, false));
    int start_r = -1, start_c = -1;

    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '.' && start_r == -1) {
                start_r = i;
                start_c = j;
            }
        }
    }

    dfs(start_r, start_c);

    for (int i = 0; i < n; ++i) {
        cout << grid[i] << '\n';
    }

    return 0;
}