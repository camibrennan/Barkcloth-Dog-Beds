 
pages = [
 
{
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Index",
},
{
    "filename": "content/purchase.html",
    "output": "docs/purchase.html",
    "title": "Purchase",
},
{
    "filename": "content/blog.html",
    "output": "docs/blog.html",
    "title": "Blog",
}
]

def read_template():
    template = open("templates/base.html").read()
    return template
    
def main():
    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
        template = read_template()
        index_content = open(page_filename).read()
        finished_index_page = template.replace("{{content}}", index_content)
        open(page_output, "w+").write(finished_index_page) 
                        
main()



