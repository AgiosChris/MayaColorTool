'''
Christian Pantoja
4/25/2019
Final Tools Programming Project
'''
import maya.cmds as mc
import random
from functools import partial
import OptionsWindowBaseClass

def cPantojaFinal():
    win = finalGUI()
    win.create()

class finalGUI(OptionsWindowBaseClass.OptionsWindow):  

    def __init__(self):
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.window = "Final Project Tool"
        self.title = "Color Selection"
        self.actionName = "Random Color"
        self.applyName = "Remove Color"
        self.myText = ""
    
    def userOption(self, result):
        if result == "Blinn":
            self.myText = "blinn"
        if result == "Phong E":
            self.myText = "phongE"
        if result == "Lambert":
            self.myText = "lambert" 
            
    def actionCmd(self, *args):
        '''
            adds a random solid color to each object in the list and removes the color
            from the cylinder and adds a texture to it.
        '''
        
        self.userSelect = mc.ls(selection = True)
        self.myShader = mc.shadingNode(self.myText, asShader = True)
        mc.select(self.userSelect)
        mc.hyperShade(assign = self.myShader)
        self.faceToVertex = mc.polyListComponentConversion( ff=True, tv=True )
        print(self.faceToVertex)
        self.Color1 = random.random()
        self.Color2 = random.random()
        self.Color3 = random.random()
        mc.setAttr(self.myShader+".colorR", self.Color1)
        mc.setAttr(self.myShader+".colorG", self.Color2)
        mc.setAttr(self.myShader+".colorB", self.Color3)
    def applyBtnCmd(self, *args):
        '''
        
        '''
        self.userSelect = mc.ls(selection = True)
        mc.sets(self.userSelect, edit = True, forceElement = "initialShadingGroup")
    def colorInput(self, *args):
        '''
    
        '''
        self.userSelect = mc.ls(selection = True)
        self.myShader = mc.shadingNode(self.myText, asShader = True)
        print(self.myShader)
        mc.select(self.userSelect)
        self.hyper = mc.hyperShade(assign = self.myShader)
        print(self.hyper)
        self.faceToVertex = mc.polyListComponentConversion( ff=True, tv=True )
        print(self.faceToVertex)
        self.Color = mc.colorInputWidgetGrp(self.Color, edit = True)
        self.colorChange = mc.colorInputWidgetGrp(self.Color, query = True, rgb = True)
        mc.setAttr(self.myShader+".colorR", self.colorChange[0])
        mc.setAttr(self.myShader+".colorG", self.colorChange[1])
        mc.setAttr(self.myShader+".colorB", self.colorChange[2])
    def displayOptions(self):
        '''
        
        '''
        ################################################
        self.myLayout = mc.rowColumnLayout("mainLayout", adjustableColumn = True, numberOfColumns = 1, cal = (1, 'left'))
        mc.text(label = "Material and Color: ")
        mc.separator(height = 20, style = "in")
        self.textLayout = mc.rowColumnLayout("userInput", adjustableColumn = True, numberOfColumns = 1, cal = (1, 'left'))
        mc.optionMenu( label='Select Material: ', changeCommand = self.userOption)
        mc.menuItem( label='')
        mc.menuItem( label='Blinn')
        mc.menuItem( label='Phong E')
        mc.menuItem( label='Lambert')
        ################################################
        self.InputLayout = mc. rowColumnLayout("inputLayout", adjustableColumn = True, numberOfRows = 1, ral = (2, 'left'))
        mc.text(label = "Select Color:")
        self.Color = mc.colorInputWidgetGrp(label = "Color", adj = 10, rgb = (0, 0, 0.271))
        mc.button(label = "Add Color Input", command = self.colorInput)

if __name__ == "__main__":
    win = finalGUI()
    win.create()
