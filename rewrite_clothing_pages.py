from pathlib import Path
import re

root = Path(r'c:\Users\DARINHIL.THA\Documents\WEB-DESIGN-PROJECT')
clothing_path = root / 'Clothing.html'
shirt_path = root / 'T-shirt.html'
shoes_path = root / 'shoes.html'
cosplay_path = root / 'cosplay.html'

clothing_html = clothing_path.read_text(encoding='utf-8')
head_start = clothing_html.index('<head>')
head_end = clothing_html.index('</head>') + len('</head>')
clothing_head = clothing_html[head_start:head_end]

# Build replacement head sections for T-shirt and shoes pages
shirt_head = clothing_head.replace('<title>Clothing - Best Anime Shop</title>', '<title>T-shirt - Best Anime Shop</title>')
shoes_head = clothing_head.replace('<title>Clothing - Best Anime Shop</title>', '<title>Shoes - Best Anime Shop</title>')

# Remove Cosplay button markup from pages
remove_cosplay_pattern = re.compile(r"\s*<a href=\"/?cosplay\.html\">\s*<button[^>]*>\s*Cosplay\s*</button>\s*</a>\s*", re.IGNORECASE)

# Replace T-shirt page head and remove cosplay button
shirt_html = shirt_path.read_text(encoding='utf-8')
shirt_html = re.sub(r'<head>[\s\S]*?</head>', shirt_head, shirt_html, flags=re.IGNORECASE)
shirt_html = shirt_html.replace('Jeacket</button>', 'Jeacket</button>')
shirt_html = remove_cosplay_pattern.sub('', shirt_html)
shirt_html = shirt_html.replace('<title>Document</title>', '<title>T-shirt - Best Anime Shop</title>')
shirt_html = shirt_html.replace('<a href="/T-shirt.html"> <button style="color: white; background: #e63946;">T-shirt</button></a>', '<a href="T-shirt.html" class="btn-gradient text-white px-6 py-2 rounded-full font-semibold text-sm">T-shirt</a>')
shirt_html = shirt_html.replace('<a href="/shoes.html"><button>Shoes</button></a>', '<a href="shoes.html" class="bg-white dark:bg-darker text-gray-700 dark:text-gray-300 px-6 py-2 rounded-full font-semibold text-sm border-2 border-gray-200 dark:border-gray-700 hover:border-primary transition-colors">Shoes</a>')
shirt_html = shirt_html.replace('<a href="Clothing.html"><button>Jeacket</button></a>', '<a href="Clothing.html" class="bg-white dark:bg-darker text-gray-700 dark:text-gray-300 px-6 py-2 rounded-full font-semibold text-sm border-2 border-gray-200 dark:border-gray-700 hover:border-primary transition-colors">Jacket</a>')
shirt_html = shirt_html.replace('<a href="/T-shirt.html"> <button style="color: white; background: #e63946;">T-shirt</button></a>', '<a href="T-shirt.html" class="btn-gradient text-white px-6 py-2 rounded-full font-semibold text-sm">T-shirt</a>')
shirt_html = shirt_html.replace('<button>Jeacket</button>', '<a href="Clothing.html" class="bg-white dark:bg-darker text-gray-700 dark:text-gray-300 px-6 py-2 rounded-full font-semibold text-sm border-2 border-gray-200 dark:border-gray-700 hover:border-primary transition-colors">Jacket</a>')
shirt_html = shirt_html.replace('<a href="/T-shirt.html"> <button>T-shirt</button></a>', '<a href="T-shirt.html" class="btn-gradient text-white px-6 py-2 rounded-full font-semibold text-sm">T-shirt</a>')

# Replace Shoes page head and remove cosplay button
shoes_html = shoes_path.read_text(encoding='utf-8')
shoes_html = re.sub(r'<head>[\s\S]*?</head>', shoes_head, shoes_html, flags=re.IGNORECASE)
shoes_html = remove_cosplay_pattern.sub('', shoes_html)
shoes_html = shoes_html.replace('<title>Document</title>', '<title>Shoes - Best Anime Shop</title>')
shoes_html = shoes_html.replace('<button>Jeacket</button>', '<a href="Clothing.html" class="bg-white dark:bg-darker text-gray-700 dark:text-gray-300 px-6 py-2 rounded-full font-semibold text-sm border-2 border-gray-200 dark:border-gray-700 hover:border-primary transition-colors">Jacket</a>')
shoes_html = shoes_html.replace('<a href="/T-shirt.html"> <button>T-shirt</button></a>', '<a href="T-shirt.html" class="bg-white dark:bg-darker text-gray-700 dark:text-gray-300 px-6 py-2 rounded-full font-semibold text-sm border-2 border-gray-200 dark:border-gray-700 hover:border-primary transition-colors">T-shirt</a>')
shoes_html = shoes_html.replace('<a href="/shoes.html"><button style="color: white; background: #e63946;">Shoes</button></a>', '<a href="shoes.html" class="btn-gradient text-white px-6 py-2 rounded-full font-semibold text-sm">Shoes</a>')

# Replace Clothing page to remove cosplay button
clothing_html = remove_cosplay_pattern.sub('', clothing_html)
clothing_html = clothing_html.replace('<button  style="color: white; background: #e63946;">T-shirt</button>', '<a href="T-shirt.html" class="bg-white dark:bg-darker text-gray-700 dark:text-gray-300 px-6 py-2 rounded-full font-semibold text-sm border-2 border-gray-200 dark:border-gray-700 hover:border-primary transition-colors">T-shirt</a>')
clothing_html = clothing_html.replace('<button>Jeacket</button>', '<a href="Clothing.html" class="btn-gradient text-white px-6 py-2 rounded-full font-semibold text-sm">Jacket</a>')
clothing_html = clothing_html.replace('<a href="/shoes.html"><button>Shoes</button></a>', '<a href="shoes.html" class="bg-white dark:bg-darker text-gray-700 dark:text-gray-300 px-6 py-2 rounded-full font-semibold text-sm border-2 border-gray-200 dark:border-gray-700 hover:border-primary transition-colors">Shoes</a>')

# Save updates
shirt_path.write_text(shirt_html, encoding='utf-8')
shoes_path.write_text(shoes_html, encoding='utf-8')
clothing_path.write_text(clothing_html, encoding='utf-8')

# Delete empty cosplay page file
if cosplay_path.exists():
    cosplay_path.unlink()
    print('Deleted cosplay.html')
else:
    print('cosplay.html not found')

print('Updated T-shirt.html, shoes.html, and Clothing.html')
