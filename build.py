 
pages = [
 
{
    "filename": "./content/index.html",
    "output": "./docs/index.html",
    "title": "Index",
},
{
    "filename": "./content/purchase.html",
    "output": "./docs/purchase.html",
    "title": "Purchase",
},
{
    "filename": "./content/blog.html",
    "output": "./docs/blog.html",
    "title": "Blog",
}
]


def main():
    for page in pages:
        page_title = page['title']
        page_filename = page['filename']
        page_output = page['output']
     
    top_html = open('./templates/top.html').read()
    bottom_html = open('./templates/bottom.html').read()
    index_html = open(page_filename).read()
    combined_html = top_html + index_html + bottom_html
    print(combined_html)
    open(page_output, 'w+').write(combined_html)

main()


 

