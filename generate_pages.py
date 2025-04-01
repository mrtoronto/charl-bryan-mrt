import csv
import json
import os
from jinja2 import Template
import re

def slugify(text):
    # Convert to lowercase and replace spaces with hyphens
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def read_products(tsv_file):
    products = []
    with open(tsv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # Skip header row
        for row in reader:
            if not row[0]:  # Skip empty rows
                continue
            product = {
                'name': row[0],
                'productLink': row[1],
                'imageUrl': row[2],
                'primarySource': row[3],
                'secondarySources': [src for src in row[4:] if src],  # Filter out empty sources
                'slug': slugify(row[0])
            }
            products.append(product)
    return products

def generate_product_pages(products):
    # Read the template
    with open('product-template.html', 'r', encoding='utf-8') as f:
        template_str = f.read()
    template = Template(template_str)

    # Create products directory if it doesn't exist
    os.makedirs('products', exist_ok=True)

    # Generate individual product pages
    for product in products:
        output = template.render(product=product)
        with open(f'products/{product["slug"]}.html', 'w', encoding='utf-8') as f:
            f.write(output)

def update_index(products):
    # Read the index.html file
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Create the products array
    products_json = []
    for product in products:
        products_json.append({
            'name': product['name'],
            'imageUrl': product['imageUrl'],
            'detailUrl': f'products/{product["slug"]}.html'
        })

    # Replace the empty products array with our data
    products_str = json.dumps(products_json, indent=8)
    updated_content = re.sub(
        r'const products = \[\];',
        f'const products = {products_str};',
        index_content
    )

    # Write the updated index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)

def main():
    products = read_products('products.tsv')
    generate_product_pages(products)
    update_index(products)

if __name__ == '__main__':
    main() 