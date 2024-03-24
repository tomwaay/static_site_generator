from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init(self, value, tag=None, props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError()
        elif self.tag == None:
            return self.value
        else:
            propshtml = self.props_to_html()
            return f'<{self.tag} {propshtml}>{self.value}</{self.tag}>'
