#http://jinja.pocoo.org/docs/2.10/api/

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('yourapplication', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('mytemplate.html')
print (template.render(the='variables', go='here'))