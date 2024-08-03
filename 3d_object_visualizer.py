import matplotlib.pyplot as plt
import numpy as np

def read_object_file(filename):
    with open(filename, 'r') as file:
        # Read the first line and split by comma if needed
        num_vertices, num_faces = map(int, file.readline().strip().split(','))
        vertices = {}
        for _ in range(num_vertices):
            line = file.readline().strip()
            # Split the line by comma for each vertex data
            id, x, y, z = line.split(',')
            vertices[int(id)] = np.array([float(x), float(y), float(z)])

        faces = []
        for _ in range(num_faces):
            line = file.readline().strip()
            # Split the line by comma for each face data
            face_ids = line.split(',')
            faces.append(list(map(int, face_ids)))

    return vertices, faces


def draw_wireframe(vertices, faces):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for face in faces:
        vtx = np.array([vertices[id] for id in face])
        ax.plot(vtx[:, 0], vtx[:, 1], vtx[:, 2], 'blue')  # Draw edges
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

filename = 'object.txt'
vertices, faces = read_object_file(filename)
draw_wireframe(vertices, faces)
                                         