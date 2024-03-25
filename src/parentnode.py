from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
    def to_html(self):
        if self.tag is None:
            raise ValueError()
        if self.children is None:
            raise ValueError("No Children")
        base = ""
        for child in self.children:
            base += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{base}</{self.tag}>'
    
