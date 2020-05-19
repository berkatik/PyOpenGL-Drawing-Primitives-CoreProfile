from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from array import array
import numpy as np
import sys

from view import *
from shapes import *
from shader import *
from defs import *
from scene import *

nVertices = None
vertexDim = 4

# String containing vertex shader program written in GLSL
strVertexShader = """
#version 330

layout(location = 0) in vec4 position;
void main()
{
   gl_Position = position;
}
"""

# String containing fragment shader program written in GLSL
strFragmentShader = """
#version 330

out vec4 outputColor;
void main()
{
   outputColor = vec4(1.0f, 1.0f, 0.0f, 1.0f);
}
"""


shader = Shader()
scene = Scene()
triangle = Triangle("Triangle", 1, 1, 0)
square = Square("Square", 1, 1, 0)
hexagon = Hexagon("Hexagon", 1, 1, 0)

scene.add(triangle)
scene.add(square)
scene.add(hexagon)

# Function that accepts a list of shaders, compiels them, and returns
# a handle to the compiled program
def createProgram(shaderList):
    programID = glCreateProgram()

    for shader in shaderList:
        glAttachShader(programID, shader)

    glLinkProgram(programID)

    status = glGetProgramiv(programID, GL_LINK_STATUS)
    if status == GL_FALSE:
        strInfoLog = gelGetProgramInfoLog(ProgramID)
        print("Linker failur: \n" + strInfoLog.decode('ascii'))

    # cleanup
    for shaderID in shaderList:
        glDetachShader(programID, shaderID)

    return programID




def initializeProgram(shader, strVertexShader, strFragmentShader):
    shaderList = []

    vertexShader = shader.createShader(GL_VERTEX_SHADER, strVertexShader)
    fragmentShader = shader.createShader(GL_FRAGMENT_SHADER, strFragmentShader)

    shaderList.append(vertexShader)
    shaderList.append(fragmentShader)

    program = createProgram(shaderList)

    for shader in shaderList:
        glDeleteShader(shader)
        
    return program


def main():
    glutInit()
    glutInitDisplayMode(GLUT_3_2_CORE_PROFILE | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    width = 500
    height = 500
    glutInitWindowSize(width, height)
    glutInitWindowPosition(300, 300)

    window = glutCreateWindow("Triangle")

    program = initializeProgram(shader, strVertexShader, strFragmentShader)
    positionBufferObject = square.initializeVertexBuffer()
    
    view = View(program, positionBufferObject, square.getVertexNum(), vertexDim, scene)
    glBindVertexArray(glGenVertexArrays(1))

    glutDisplayFunc(view.display)
    glutKeyboardFunc(view.keyboard)
    
    print("Press key 1 for triangle. \nPress key 2 for square. \nPress key 3 for Hexagon. \nPress ESC to quit.")

    glutMainLoop()



if __name__ == '__main__':
    main()
