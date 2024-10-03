from math import sqrt


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_dotpair(X: tuple[tuple[float | int, float | int], ...], Y: tuple[tuple[float | int, float | int], ...]) -> tuple[tuple[tuple[float | int, float | int], tuple[float | int, float | int]], float | int]:
    n = len(X)
    # n <= 3 时，暴力求解
    if n <= 3:
        point_pair = ((0, 0), (float('inf'), float('inf')))
        dist_min = float('inf')
        for i in range(n - 1):
            for j in range(i + 1, n):
                if distance(X[i], X[j]) < dist_min:
                    dist_min = distance(X[i], X[j])
                    point_pair = (X[i], X[j])
        return (point_pair, dist_min)
    half = n // 2
    XL = X[:half]
    XR = X[half:]
    XL_set = set(XL)
    XR_set = set(XR)
    YL = tuple(pt for pt in Y if pt in XL_set)
    YR = tuple(pt for pt in Y if pt in XR_set)
    left_res = find_dotpair(XL, YL)
    right_res = find_dotpair(XR, YR)
    point_pair = left_res[0] if left_res[1] < right_res[1] else right_res[0]
    dist_min = left_res[1] if left_res[1] < right_res[1] else right_res[1]
    x_mid_pos = (X[half - 1][0] + X[half][0]) / 2
    Y_midarea = [dot for dot in Y if dot[0] >= x_mid_pos - dist_min and dot[0] <= x_mid_pos + dist_min]
    for i in range(len(Y_midarea)):
        for j in range(i + 1, i + 6):
            if j >= len(Y_midarea):
                break
            if distance(Y_midarea[i], Y_midarea[j]) < dist_min:
                dist_min = distance(Y_midarea[i], Y_midarea[j])
                point_pair = (Y_midarea[i], Y_midarea[j])
    return (point_pair, dist_min)


def closest_pair_helper(points: tuple[tuple[float | int, float | int], ...]) -> tuple[tuple[float | int, float | int], tuple[float | int, float | int]]:
    X = tuple(sorted(points, key=lambda it: (it[0], it[1])))
    for i in range(len(X) - 1):
        if X[i] == X[i + 1]:
            return (X[i], X[i + 1])
    Y = tuple(sorted(points, key=lambda it: it[1]))
    ans = find_dotpair(X, Y)
    return ans[0]


def closest_pair(points):
    return closest_pair_helper(points)


if __name__ == "__main__":
    points = (
        (2, 2),  # A
        (2, 8),  # B
        (5, 5),  # C
        (6, 3),  # D
        (6, 7),  # E
        (7, 4),  # F
        (7, 9)   # G
    )
    print(closest_pair(points))
