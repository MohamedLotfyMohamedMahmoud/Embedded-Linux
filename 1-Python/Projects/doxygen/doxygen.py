import pandas as pd
from bs4 import BeautifulSoup

input_html_file = 'example.html'  # Replace with your HTML file name

try:
    # Read HTML content from the file
    with open(input_html_file, 'rb') as f:
        html_content = f.read()

    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract data
    products = []
    product_elements = soup.find_all('div', class_='product')
    for product in product_elements:
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('p', class_='product-price').text.strip()
        products.append({'Product Name': name, 'Price': price})

    # Create DataFrame
    df = pd.DataFrame(products)

    # Save to Excel
    output_excel_file = 'products_data.xlsx'
    df.to_excel(output_excel_file, index=False)
    print(f"Data successfully written to {output_excel_file}")

except FileNotFoundError:
    print(f"HTML file '{input_html_file}' not found. Please make sure the file exists.")

except Exception as e:
    print(f"An error occurred: {e}")
