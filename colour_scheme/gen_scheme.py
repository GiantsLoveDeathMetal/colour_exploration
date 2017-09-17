from templates import grab_template

background='#000000'
global_text='#c0c0c0'
operational='#808000'
operator='#808000'
strings='#800000'
ints='#ff00ff'
key_words='#cf6a4c'
def_functions='#cf6a4c'
class_colour='#d80a52'
doc_strings='#666666'
comments='#008000'


fit_template = grab_template().format(
    background=background,
    global_text=global_text,
    operational=operational,
    operator=operator,
    strings=strings,
    ints=ints,
    key_words=key_words,
    def_functions=def_functions,
    class_colour=class_colour,
    doc_strings=doc_strings,
    comments=comments
)


def save_html(html_text):
    save_as = 'new_template.html'

    with open(save_as, 'w') as html_file:
        html_file.write(html_text)
        
save_html(fit_template)