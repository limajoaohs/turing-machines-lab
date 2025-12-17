#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long x0, y0, x1, y1;
    cin >> x0 >> y0 >> x1 >> y1;

    int n;
    cin >> n;

    map<long long, vector<pair<long long, long long>>> segments;
    for (int i = 0; i < n; ++i) {
        long long r, a, b;
        cin >> r >> a >> b;
        segments[r].push_back({a, b});
    }

    for (auto const& [row, segs] : segments) {
        sort(segments[row].begin(), segments[row].end());
        vector<pair<long long, long long>> merged;
        if (!segs.empty()) {
            merged.push_back(segs[0]);
            for (size_t i = 1; i < segs.size(); ++i) {
                if (segs[i].first <= merged.back().second + 1) {
                    merged.back().second = max(merged.back().second, segs[i].second);
                } else {
                    merged.push_back(segs[i]);
                }
            }
        }
        segments[row] = merged;
    }

    queue<pair<long long, long long>> q;
    map<pair<long long, long long>, int> dist;

    q.push({x0, y0});
    dist[{x0, y0}] = 0;

    int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    while (!q.empty()) {
        pair<long long, long long> curr = q.front();
        q.pop();

        long long r = curr.first;
        long long c = curr.second;
        int d = dist[curr];

        if (r == x1 && c == y1) {
            cout << d << endl;
            return 0;
        }

        for (int i = 0; i < 8; ++i) {
            long long nr = r + dr[i];
            long long nc = c + dc[i];
            pair<long long, long long> next_pos = {nr, nc};

            if (segments.count(nr)) {
                auto it = upper_bound(segments[nr].begin(), segments[nr].end(), make_pair(nc, -1LL));
                if (it != segments[nr].begin()) {
                    it--;
                    if (nc >= it->first && nc <= it->second) {
                        if (dist.find(next_pos) == dist.end()) {
                            dist[next_pos] = d + 1;
                            q.push(next_pos);
                        }
                    }
                }
            }
        }
    }

    cout << -1 << endl;

    return 0;
}