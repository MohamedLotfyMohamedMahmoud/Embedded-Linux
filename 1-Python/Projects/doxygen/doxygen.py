""" 
import csv
from bs4 import BeautifulSoup

fs = open("doc/generated/html/classstd1_Hello.html", "r")
html_content = fs.read()
fs.close()

print(html_content)

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
functions = []
# find memdoc class
contents = soup.find('div', class_='contents')
allfunctions = contents.find_all('h2', class_='memtitle')
allmemitem = contents.find_all('div', class_='memitem')
allsignatures = []
allbrief = []
allparams = []
all_returns = []

for memitem in allmemitem:
    signature = memitem.find('td', class_='memname').text
    brief = memitem.find('div', class_='memdoc').find('p').text
    paramtable = memitem.find('table', class_='params').find_all('td', class_='paramname')
    return_ = memitem.find('div', class_='memdoc').find('dl', class_='section return').find('dd').text
    paramlist = []
    
    for param in paramtable:
        paramlist.append(param.text)
    
    all_returns.append(return_)
    allparams.append(paramlist)
    allsignatures.append(signature)
    allbrief.append(brief)

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Signature', 'Brief', 'Parameters', 'Return'])
    
    for i in range(len(allfunctions)):
        writer.writerow([allsignatures[i], allbrief[i], ', '.join(allparams[i]), all_returns[i]])
 """
##################################################################################################################
""" import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the webpage content
url = "https://www.yallakora.com/"
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Debug: Print the entire HTML content or part of it to inspect the structure
# print(soup.prettify())  # Uncomment this line to print the HTML content

# Extract match details
# Note: Update these class names based on the actual structure of Yallakora's webpage
matches = soup.find_all('div', class_='matchDetails')

# Debug: Print the number of matches found
print(f"Found {len(matches)} matches.")

# Lists to hold extracted data
all_matches = []
all_scores = []
all_dates = []

# Loop through the matches and extract details
for match in matches:
    teams = match.find_all('div', class_='team')
    
    # Debug: Print the teams element to verify it contains the expected data
    print("Teams Element:", teams)
    
    if teams and len(teams) >= 2:
        team1 = teams[0].text.strip()
        team2 = teams[1].text.strip()
        score = match.find('div', class_='score').text.strip() if match.find('div', class_='score') else "N/A"
        date = match.find('div', class_='date').text.strip() if match.find('div', class_='date') else "N/A"
        
        # Debug: Print extracted details for each match
        print(f"Match: {team1} vs {team2}, Score: {score}, Date: {date}")

        all_matches.append(f"{team1} vs {team2}")
        all_scores.append(score)
        all_dates.append(date)
    else:
        # Debug: Print a message if teams data is not found
        print("Teams data not found for a match.")

# Debug: Print lists to verify data before creating DataFrame
print("Matches:", all_matches)
print("Scores:", all_scores)
print("Dates:", all_dates)

# Create a DataFrame
df = pd.DataFrame({
    'Match': all_matches,
    'Score': all_scores,
    'Date': all_dates
})

# Debug: Print the DataFrame to verify the extracted data
print(df)

# Save the data to an Excel file
df.to_excel('yallakora_matches.xlsx', index=False)

print("Data successfully written to yallakora_matches.xlsx")
 """

##########################################################################################################################
""" import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.yallakora.com/file.html'  # Replace with the actual URL of the file you want to download
output_file = 'file.html'  # Specify the name you want to save the file as locally

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Write the contents of the response to the local file
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded successfully as '{output_file}'")
else:
    print(f"Failed to download file: Status code {response.status_code}")





fs = open("file.html", "r")
html_content = fs.read()
fs.close()

print(html_content)

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
functions = []
# find memdoc class
contents = soup.find('div', class_='contents')
allfunctions = contents.find_all('h2', class_='memtitle')
allmemitem = contents.find_all('div', class_='memitem')
allsignatures = []
allbrief = []
allparams = []
all_returns = []

for memitem in allmemitem:
    signature = memitem.find('td', class_='memname').text
    brief = memitem.find('div', class_='memdoc').find('p').text
    paramtable = memitem.find('table', class_='params').find_all('td', class_='paramname')
    return_ = memitem.find('div', class_='memdoc').find('dl', class_='section return').find('dd').text
    paramlist = []
    
    for param in paramtable:
        paramlist.append(param.text)
    
    all_returns.append(return_)
    allparams.append(paramlist)
    allsignatures.append(signature)
    allbrief.append(brief)

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Signature', 'Brief', 'Parameters', 'Return'])
    
    for i in range(len(allfunctions)):
        writer.writerow([allsignatures[i], allbrief[i], ', '.join(allparams[i]), all_returns[i]])
 """
##########################################################################################################################


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
