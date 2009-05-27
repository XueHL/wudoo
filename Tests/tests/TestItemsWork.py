import unittest, os

from wudoo.FSItem import FSItem 

class TestItemsWork(unittest.TestCase):
    def testItem(self):
        #print "Ignore"; return
        stepA = os.path.join("A0", "A1", "A2")
        stepB = os.path.join("B0", "B1", "B2")
        stepC = os.path.join("C0", "C1", "C2")
        name = "name" + "." + "ext"
        fsItem = FSItem(stepA, stepB, stepC, name)
        
        self.assertEquals(os.path.join("A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2", "name.ext"), fsItem.getPathNameExt())
        self.assertEquals(os.path.join("A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2", "name.ext"), fsItem.getPathNameExt(0))
        self.assertEquals(os.path.join("B0", "B1", "B2", "C0", "C1", "C2", "name.ext"), fsItem.getPathNameExt(1))
        self.assertEquals(os.path.join("C0", "C1", "C2", "name.ext"), fsItem.getPathNameExt(2))
        
        self.assertEquals("ext", fsItem.getExt())
        self.assertEquals("name", fsItem.getName())

        self.assertEquals(os.path.join("A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2"), fsItem.getPath())
        self.assertEquals(os.path.join("A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2"), fsItem.getPath(0))
        self.assertEquals(os.path.join("B0", "B1", "B2", "C0", "C1", "C2"), fsItem.getPath(1))
        self.assertEquals(os.path.join("C0", "C1", "C2"), fsItem.getPath(2))
        
        self.assertEquals(os.path.join("A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2"), fsItem.getBegOfPath())
        self.assertEquals(os.path.join("A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2"), fsItem.getBegOfPath(3))
        self.assertEquals(os.path.join("A0", "A1", "A2", "B0", "B1", "B2"), fsItem.getBegOfPath(2))
        self.assertEquals(os.path.join("A0", "A1", "A2"), fsItem.getBegOfPath(1))
