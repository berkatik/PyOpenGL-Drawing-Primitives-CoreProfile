from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np

class Shader:
    # Function that creates and compiles shaders according to the given
    # type (a GL enum value) and shader program (a string containin a glsl program).
    def createShader(self, shaderType, shaderFile):
        shaderID = glCreateShader(shaderType)
        glShaderSource(shaderID, shaderFile)
        glCompileShader(shaderID)

        status = None
        glGetShaderiv(shaderID, GL_COMPILE_STATUS, status)
        if status == GL_FALSE:
            strInfoLog = glGetShaderInfoLog(shaderID)
            strShaderType = ""
            if shaderType is GL_VERTEX_SHADER:
                strShaderType = "vertex"
            elif shaderType is GL_GEOMETRY_SHADER:
                strShaderType = "geometry"
            elif shaderType is GL_FRAGMENT_SHADER:
                strShaderType = "fragment"

            print("Compilation failure for " + strShaderType + " shader:\n" + strInfoLog)

        
        return shaderID

