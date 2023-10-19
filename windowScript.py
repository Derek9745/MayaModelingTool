import maya.cmds as cmds

def windowButton(args):
    windowFrame = cmds.polyCube()
    cmds.scale(3,3,.25)
    cutOut = cmds.polyCube()
    cmds.scale(2,2,1.3)
    cmds.polyBooleanCmd(windowFrame,cutOut, operation = 2)
    cmds.delete(windowFrame,cutOut)
 

def pipeButton(args):
    pipe1 = cmds.polyCylinder()
    pipe2 = cmds.polyCylinder()
    cmds.rotate(0,0,90,pipe1)
    cmds.move(3,3,0,pipe1)
    pipe3 = cmds.polyUnite(pipe1,pipe2, n = 'result')
    #cmds.select(pipe3.f[43],pipe3.f[21])
    #cmds.polyBridgeEdge('result.e[20:39]','result.e[80:99]', divisions = 10, curveType = 1, sourceDirection =1)
 
    
    
def floorButton(args):
    floortile = cmds.polyCube()
    cmds.scale(5,.125,5, floortile)
    
def hollowPipeButton(args):
    cmds.polyPipe()
    
 
class CreateWindow(object):
    def __init__(self):
        self.window = "CreateWindow"
        self.title = "Advanced Polygon Creator"
        self.size = (400, 400)
        
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window = True)
            
        self.window = cmds.window(self.window, title = self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn = True)
        cmds.text(self.title)
        cmds.separator(height = 20)
        cmds.button(label ="Create Angle Pipe", command = pipeButton) 
        cmds.separator(height = 20)
        cmds.button(label ="Create Floor Tile", command = floorButton)
        cmds.separator(height = 20)
        cmds.button(label ="Create Window Frame", command = windowButton)
        cmds.separator(height = 20)
        cmds.button(label ="Create a Hollow Pipe", command = hollowPipeButton)
        cmds.showWindow()

myWindow = CreateWindow()




