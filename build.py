import glob
import os

all_html_files = glob.glob('content/*.html')

def get_filename(file_path): 
    file_name = os.path.basename(file_path)

def get_psge_title(file_path): 
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    title = name_only
    return title
     
def get_output_file(file_path):  
    file_name = os.path.basename(file_path)
    text = file_path
    output_file_path = text.replace('content', 'docs')
    return output_file_path

pages = []
for file_path in all_html_files:
    pages.append({
    "filename": file_path,
    "title": get_psge_title(file_path),
    "output": get_output_file(file_path),
    })
    print(pages)

from jinja2 import Template
index_html = open("content/index.html").read()

template_html = open("templates/base.html").read()
template = Template(template_html)
template.render(
    title="title",
    content=index_html,
)




# def read_template():
#     template = open("templates/base.html").read()
#     return template

# def apply_template(page_filename, page_output, page_title):
#     template = read_template()
#     index_content = open(page_filename).read()
#     finished_index_page = template.replace("{{content}}", index_content).replace("{{title}}", page_title)
#     open(page_output, "w+").write(finished_index_page) 
#     return finished_index_page

             
# main()


