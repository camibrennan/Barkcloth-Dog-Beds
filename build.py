#index
top_html = open('./templates/top.html').read()
bottom_html = open('./templates/bottom.html').read()
index_html = open('./content/index.html').read()
combined_html = top_html + index_html + bottom_html
print(combined_html)
open('./docs/index.html', 'w+').write(combined_html)

# purchase
top_html = open('./templates/top.html').read()
bottom_html = open('./templates/bottom.html').read()
purchase_html = open('./content/purchase.html').read()
combined_html = top_html + purchase_html + bottom_html
print(combined_html)
open('./docs/purchase.html', 'w+').write(combined_html)

#blog
top_html = open('./templates/top.html').read()
bottom_html = open('./templates/bottom.html').read()
blog_html = open('./content/blog.html').read()
combined_html = top_html + blog_html + bottom_html
print(combined_html)
open('./docs/blog.html', 'w+').write(combined_html)