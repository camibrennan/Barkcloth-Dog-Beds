import glob
import os
from jinja2 import Template

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

def create_new_page():
    open('content/new_page.html', 'w+').write('<h1>New Content!</h1><p>New content...</p>')

pages = []
for file_path in all_html_files:
    pages.append({
    "filename": file_path,
    "title": get_psge_title(file_path),
    "output": get_output_file(file_path),
    })


def main():
    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']

        template = Template(open("templates/base.html").read())
        html_result = template.render(
            title=page['title'],
            content=open(page['filename']).read(),
        )
        open(page['output'], 'w+').write(html_result)


