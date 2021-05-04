import pygame
import os
import math
from matrix import *
from icosphere import *

os.environ["SDL_VIDEO_CENTERED"] = '1'
black, white, blue = (20, 20, 20), (230, 230, 230), (0, 154, 255)
width, height = 1080, 700  # 1920, 1080

pygame.init()
pygame.display.set_caption("3D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

angle = 0
cube_position = [width // 2, height // 2]
scale = 600
speed = 0.01
points = [n for n in range(8)]

points[0] = [[-1], [-1], [1], [1]]
points[1] = [[1], [-1], [1], [1]]
points[2] = [[1], [1], [1], [1]]
points[3] = [[-1], [1], [1], [1]]
points[4] = [[-1], [-1], [-1], [1]]
points[5] = [[1], [-1], [-1], [1]]
points[6] = [[1], [1], [-1], [1]]
points[7] = [[-1], [1], [-1], [1]]
x = 10

def connect_point(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, black, (a[0], a[1]), (b[0], b[1]), 2)


run = True
while run:
    clock.tick(fps)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 3
                print('12313414123414')
            elif event.key == pygame.K_RIGHT:
                x += 3

    index = 0
    projected_points = [j for j in range(len(points))]

    rotation_x = [[1, 0, 0, 0],
                  [0, math.cos(angle), -math.sin(angle), 0],
                  [0, math.sin(angle), math.cos(angle), 0],
                  [0, 0, 0, 1]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle), 0],
                  [0, 1, 0, 0],
                  [math.sin(angle), 0, math.cos(angle), 0],
                  [0, 0, 0, 1]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0, 0],
                  [math.sin(angle), math.cos(angle), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]

    translate = [[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]]
    eye = [[x], [1], [10]]
    look_at = [[x + 10], [1], [10]]
    w = get_vector(eye, look_at)
    up = [eye[0], eye[1], [eye[2][0] + 1], 1]
    v = cross_product(w, up)
    u = cross_product(w, v)
    x0 = -dot_product(eye, u)
    y0 = -dot_product(eye, v)
    z0 = -dot_product(eye, w)
    basis_change = [[u[0][0], u[1][0], u[2][0], x0],
                    [v[0][0], v[1][0], v[2][0], x0],
                    [w[0][0], w[1][0], w[2][0], x0],
                    [0, 0, 0, 1]]
    print(basis_change)
    for point in points:
        rotated_2d = matrix_multiplication(rotation_y, point)
        rotated_2d = matrix_multiplication(rotation_x, rotated_2d)
        rotated_2d = matrix_multiplication(rotation_z, rotated_2d)
        translated_2d = matrix_multiplication(translate, rotated_2d)
        basis_changed = matrix_multiplication(basis_change, translated_2d)
        distance = 5

        #z = 1 / (distance - translated_2d[2][0])
        z = distance / basis_changed[2][0]
        projection_matrix = [[z, 0, 0, 0],
                             [0, z, 0, 0]]

        projected_2d = matrix_multiplication(projection_matrix, basis_changed)#translated_2d)
        x = int(projected_2d[0][0] * scale) + cube_position[0]
        y = int(projected_2d[1][0] * scale) + cube_position[1]
        projected_points[index] = [x, y]
        pygame.draw.circle(screen, blue, (x, y), 10)
        index += 1
    # draw edges

    for m in range(4):
        connect_point(m, (m + 1) % 4, projected_points)
        connect_point(m + 4, (m + 1) % 4 + 4, projected_points)
        connect_point(m, m + 4, projected_points)

    angle += speed
    pygame.display.update()

pygame.quit()
