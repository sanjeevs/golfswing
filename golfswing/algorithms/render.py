from golfswing.graph2d import draw, line, screen

def lst_to_points(lst):
    """ Given a list of int return a lst of pairs. """
    if len(lst) % 2:
        raise IndexError("Lst must have even length")
    points = []
    for i in range(0, len(lst), 2):
        points.append((lst[i], lst[i + 1]))
    return points

def render(frame, screen_desc):
    """
    Reders the objects described in screen desc on the incoming frame.
    :param frame: incoming frame that is modified.
    :param screen_desc: Associaitve array
    :return: None
    """
    for key, value in screen_desc.items():
        if key == "TargetLine":
            points = lst_to_points(value)
            draw.target_line(frame, points[0])

        if key == "ClubLine":
            points = lst_to_points(value)
            # FIXME: use the entire x axis to draw the club.
            club = line.Line(points[0], points[1])
            draw.club_line(frame, club, 0, screen.WIDTH)

        if key == "SwingPlane":
            points = lst_to_points(value)
            plane = draw.Parallelogram(points[0], points[1], points[2],
                               points[3])
            draw.swing_plane(frame, plane)

