import math


class _PointWrapper:

    def __init__(self, point, base):
        self.point = point
        self.base = base
        self.polar_angle = math.degrees(math.atan2(point.y - base.y, point.x - base.x))
        dx = point.x - base.x
        dy = point.y - base.y
        self.distance = math.sqrt(dx*dx + dy*dy)

    def __str__(self):
        return "%s, (%s, %s), polar_angle = %.1F, distance = %.1F" % \
               (self.point.name, self.point.x, self.point.y, self.polar_angle, self.distance)

    __repr__ = __str__


def _find_base_point(points):
    """
    Returns the point with the minimum y-coordinate,
    or the leftmost such point in case of a tie.
    """

    base_point = points[0]

    for i in range(1, len(points)):

        cur = points[i]

        if cur.y < base_point.y or (cur.y == base_point.y and cur.x < base_point.x):
            base_point = cur

    return base_point


def _not_left_turn(p1, p2, p3):
    """
    Three points are a counter-clockwise turn if ccw > 0, clockwise if
    ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
    gives twice the signed area of the triangle formed by p1, p2 and p3.
    """
    ccw = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    return ccw <= 0


def _prepare_points(points, left_point):
    """
    sort the points by 'polar_angle', then by 'distance', remove with duplicate 'polar_angle' (left the farthest one)
    """

    sorted_points = [_PointWrapper(val, left_point) for val in points if val != left_point]
    sorted_points.sort(key=lambda pw: (pw.polar_angle, pw.distance))

    res = [sorted_points[0]]

    for i in range(1, len(sorted_points)):

        cur = sorted_points[i]
        last_in_res = res[len(res)-1]

        if last_in_res.polar_angle == cur.polar_angle and cur.distance > last_in_res.distance:
            res[len(res)-1] = cur
        else:
            res.append(sorted_points[i])

    return res


def convex_hull(points):
    """
    Construct convex hull using Graham's scan.
    Time O(n*lgN), space: O(N)
    """

    if len(points) < 3:
        raise ValueError("Can't create convex hull with less then 3 points")

    polygon = []

    base_point = _find_base_point(points)
    polygon.append(base_point)

    sorted_points = _prepare_points(points, base_point)

    if len(sorted_points) < 2:
        raise ValueError("Can't create convex hull with less then 3 points")

    polygon.append(sorted_points[0].point)
    polygon.append(sorted_points[1].point)

    for i in range(2, len(sorted_points)):

        cur = sorted_points[i].point

        while True:
            top = polygon[len(polygon)-1]
            top_next = polygon[len(polygon)-2]

            if _not_left_turn(top_next, top, cur):
                polygon.pop()
            else:
                break

        polygon.append(cur)

    return polygon


def farthest_points(points):
    """
    Find farthest pair of points. This pair of
    points should lie on convex hull.
    """
    hull_points = convex_hull(points)

    # todo
    return hull_points[0], hull_points[1]