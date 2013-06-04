from django.template import Library, Node
register = Library()


class PydevDebugNode(Node):
    def render(self, context):
        try:
            import pydevd #@UnresolvedImport
            pydevd.connected = True
            pydevd.settrace()
            return ''
        except:
            # It might be more clear to just let this exception pass through
            return 'Debugger was not turned on'

@register.tag
def template_debug(parser, token):
    return PydevDebugNode()
