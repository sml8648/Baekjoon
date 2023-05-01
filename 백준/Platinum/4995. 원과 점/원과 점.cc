#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

typedef pair<double, double> Point;

double dist(const Point& a, const Point& b) {
    return sqrt(pow(a.first - b.first, 2) + pow(a.second - b.second, 2));
}

bool isInsideCircle(const Point& center, const Point& p) {
    return dist(center, p) <= 1.0 + 1e-9;
}

int main() {
    int N;
    while (cin >> N && N) {
        vector<Point> points(N);
        for (int i = 0; i < N; i++) {
            double x, y;
            cin >> x >> y;
            points[i] = make_pair(x, y);
        }

        int max_points = 1;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                double d = dist(points[i], points[j]);
                if (d > 2.0) continue;

                double angle = acos(d / 2.0);
                double mid_x = (points[i].first + points[j].first) / 2.0;
                double mid_y = (points[i].second + points[j].second) / 2.0;
                double dx = points[j].first - points[i].first;
                double dy = points[j].second - points[i].second;

                for (int dir = 0; dir < 2; dir++) {
                    double shift = dir ? angle : -angle;
                    double x = mid_x + sin(shift) * dy / d;
                    double y = mid_y - sin(shift) * dx / d;
                    Point center = make_pair(x, y);

                    int count = 0;
                    for (const auto& p : points) {
                        if (isInsideCircle(center, p)) {
                            count++;
                        }
                    }
                    max_points = max(max_points, count);
                }
            }
        }

        cout << max_points << endl;
    }

    return 0;
}
