class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    #try implementing base as a list and append all the strings to join into one before return
    def props_to_html(self):
        base = ""
        if self.props != None:
            for key in self.props:
                base += f' {key}="{self.props[key]}"'
        return base
        
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children},{self.props})"