import numpy as np

def closer_point(pointA, pointBs):
    dists = np.array([np.hypot(pointA[0]-pb[0], pointA[1]-pb[1]) for pb in pointBs])
    idx = dists.argmin()
    return pointBs[idx]

def both_intersections(x0, y0, r0, x1, y1, r1):
    d = np.hypot(x1 - x0, y1 - y0)
    a = (r0**2 - r1**2 + d**2) / (2 * d)
    h_sq = r0**2 - a**2
    if h_sq < 0:
        h_sq = 0.0
    h = np.sqrt(h_sq)
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d
    rx = -(y1 - y0) * (h / d)
    ry =  (x1 - x0) * (h / d)
    xi1, yi1 = x2 + rx, y2 + ry
    xi2, yi2 = x2 - rx, y2 - ry
    return [[xi1, yi1], [xi2, yi2]]

def calculate_trajectory(chromosome, angle=1, resolution=100, return_all=False):

    J1x, J1y = chromosome.J1x, chromosome.J1y
    J5x, J5y = chromosome.J5x, chromosome.J5y
    genome = chromosome.genome
    trajectory = []
    for _ in np.linspace(0, 360, num=resolution):
        J4x = J1x + genome.L14 * np.cos(np.radians(_))
        J4y = J1y + genome.L14 * np.sin(np.radians(_))
        if _ == 0:
            J2x, J2y = both_intersections(genome.J3x, genome.J3y, genome.L32,
                                        J4x, J4y, genome.L24)[0]
            J7x, J7y = both_intersections(J4x, J4y, genome.L47,
                                        J2x, J2y, genome.L27)[0]
        else:
            J2x, J2y = closer_point((J2x, J2y), both_intersections(genome.J3x, genome.J3y, genome.L32,
                                        J4x, J4y, genome.L24))
            J7x, J7y = closer_point((J7x, J7y), both_intersections(J4x, J4y, genome.L47,
                                    J2x, J2y, genome.L27))
        J6x, J6y = both_intersections(J5x, J5y, genome.L56,
                                    J7x, J7y, genome.L67)[1]
        J8x, J8y = both_intersections(J6x, J6y, genome.L68,
                                    J7x, J7y, genome.L87)[1]
        if return_all:
            trajectory.append([float(J1x), float(J1y), float(J2x), float(J2y),
                                 float(genome.J3x), float(genome.J3y),
                               float(J4x), float(J4y), float(J5x), float(J5y),
                               float(J6x), float(J6y), float(J7x), float(J7y),
                               float(J8x), float(J8y)])
        else:
            trajectory.append([float(J7x), float(J7y), float(J8x), float(J8y)])
    return trajectory