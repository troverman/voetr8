if request.function == 'index':
    response.title = 'voetr'
else:
    response.title = request.function

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Trevor Overman'
response.meta.description = 'empowering the internet'
response.meta.keywords = 'voting, empowerment, internet'
response.meta.generator = 'Web2py Web Framework'
