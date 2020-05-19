from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


class _Shape:
    def __init__(self, name, vertices):
        self.vertices = np.array(vertices, dtype='float32')
        # self.edges = []
        # self.faces = numpy.asarray(faces, dtype=numpy.int64)
        self.name = name

    # Set up the vertex buffer that will store our vertex 
    # coordsinates for OpenGL's access
    def initializeVertexBuffer(self):
        positionBufferObject = glGenBuffers(1)

        # Set array buffer to our ID
        glBindBuffer(GL_ARRAY_BUFFER, positionBufferObject)
        glBufferData(
            GL_ARRAY_BUFFER,
            self.vertices,
            GL_STATIC_DRAW
        )

        # Reset array buffeer
        glBindBuffer(GL_ARRAY_BUFFER, 0)
    
        return positionBufferObject

    def getVertexNum(self):
        return self.vertices.shape[0]

class Triangle(_Shape):
    def __init__(self, name, xSize, ySize, zSize):
        vertices = []

        vertices.extend([0, ySize / 2.0, 0, 1.0])
        vertices.extend([xSize / 2.0, -ySize / 2.0, 0, 1.0])
        vertices.extend([-xSize / 2.0, -ySize / 2.0, 0, 1.0])

        _Shape.__init__(self, name, vertices)

class Square(_Shape):
    def __init__(self, name, xSize, ySize, zSize):
        vertices = []

        vertices.extend([-xSize / 2.0, ySize / 2.0, zSize, 1.0])
        vertices.extend([xSize / 2.0, ySize / 2.0, zSize, 1.0])
        vertices.extend([xSize / 2.0, -ySize / 2.0, zSize, 1.0])
        
        vertices.extend([xSize / 2.0, -ySize / 2.0, zSize, 1.0])
        vertices.extend([-xSize / 2.0, -ySize / 2.0, zSize, 1.0])
        vertices.extend([-xSize / 2.0, ySize / 2.0, zSize, 1.0])

        _Shape.__init__(self, name, vertices)

class Hexagon(_Shape):
    def __init__(self, name, xSize, ySize, zSize):
        vertices = []

        vertices.extend([-xSize / 4.0, ySize / 2.0, zSize, 1.0])
        vertices.extend([0.0, 0.0, zSize, 1.0])
        vertices.extend([xSize / 4.0, ySize / 2.0 , zSize, 1.0])
        
        vertices.extend([xSize / 4.0, ySize / 2.0 , zSize, 1.0])
        vertices.extend([0.0, 0.0, zSize, 1.0])
        vertices.extend([xSize / 2.0, 0.0, zSize, 1.0])
        
        vertices.extend([xSize / 2.0, 0.0, zSize, 1.0])
        vertices.extend([0.0, 0.0, zSize, 1.0])
        vertices.extend([xSize / 4.0, -ySize / 2.0, zSize, 1.0])
        
        vertices.extend([xSize / 4.0, -ySize / 2.0, zSize, 1.0])
        vertices.extend([0.0, 0.0, zSize, 1.0])
        vertices.extend([-xSize / 4.0, -ySize / 2.0, zSize, 1.0])
        
        vertices.extend([-xSize / 4.0, -ySize / 2.0, zSize, 1.0])
        vertices.extend([0.0, 0.0, zSize, 1.0])
        vertices.extend([-xSize / 2.0, 0.0, zSize, 1.0])

        vertices.extend([-xSize / 2.0, 0.0, zSize, 1.0])
        vertices.extend([0.0, 0.0, zSize, 1.0])
        vertices.extend([-xSize / 4.0, ySize / 2.0, zSize, 1.0])

        _Shape.__init__(self, name, vertices)