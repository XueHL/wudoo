from wudoo.textproc.document.elements.BaseCompositElement import BaseCompositElement

class Paragraph(BaseCompositElement):
	def __init__(self):
		BaseCompositElement.__init__(self)

	def visit(self, visitor):
		visitor.visitParagraph(self)
