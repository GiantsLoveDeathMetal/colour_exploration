
def grab_template(name_template='template.html'):

    open_file = 'html_src/{html_name}'.format(html_name=name_template)
    
    with open(open_file) as load_file:
        file_contents = load_file.read()
        
    return file_contents
