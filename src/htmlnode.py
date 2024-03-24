class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        base = ""
        if self.props is None:
            return base
        for key in self.props:
            base += f' {key}="{self.props[key]}"'
        return base
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children},{self.props})"
    

