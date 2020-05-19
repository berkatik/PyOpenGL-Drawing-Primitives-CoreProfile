from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np

from defs import *
from scene import *
from shapes import *

class View:
    def __init__(self, program, positinBufferObject, nVertices, vertexDim, scene = None):
        self.program = program
        self.positionBufferObject = positinBufferObject
        self.nVertices = nVertices
        self.vertexDim = vertexDim
        self.scene = scene

    def sefScene(self, scene):
        self.scene = scene


    # Called to update the display.
    # Because we are using double-buffering, glutSwapBuffers is called at the end
    # to write the rendered buffer to display
    def display(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Use our program
        glUseProgram(self.program)

        # Reset out vertex buffer
        glBindBuffer(GL_ARRAY_BUFFER, self.positionBufferObject)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, self.vertexDim, GL_FLOAT, GL_FALSE, 0, None)

        glDrawArrays(GL_TRIANGLES, 0, self.nVertices)

        glDisableVertexAttribArray(0)
        glUseProgram(0)

        glutSwapBuffers()

    def keyboard(self, *args):
        if args[0] == ESCAPE:
            sys.exit()
            return

        if args[0] == Shape.TRIANGLE:
            obj = self.scene.nodes[0]
            self.nVertices = obj.getVertexNum()
            self.positionBufferObject = obj.initializeVertexBuffer()
            self.display()
            return

        if args[0] == Shape.SQUARE:
            obj = self.scene.nodes[1]
            self.nVertices = obj.getVertexNum()
            self.positionBufferObject = obj.initializeVertexBuffer()
            self.display()
            return

        if args[0] == Shape.HEXAGON:
            obj = self.scene.nodes[2]
            self.nVertices = obj.getVertexNum()
            self.positionBufferObject = obj.initializeVertexBuffer()
            self.display()
            return

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
