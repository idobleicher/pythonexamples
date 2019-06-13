#contextlib.ContextDecorator  lets you define a context manager using the class-based approach, but inheriting from contextlib.ContextDecorator.
# By doing so, you can use your context manager with the with statement as normal or as a function decorator
from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False


@makeparagraph()
def emit_html():
    print('Here is some non-HTML')

emit_html()
