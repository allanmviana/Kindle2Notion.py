# Importing libraries
import sys
import os
from bs4 import BeautifulSoup

# Get the file localization. Desktop as default
os.chdir('C:/Users/allan/Desktop')
file_loc = input("What is the file name? \n")

#Importing the file
with open(str(file_loc) + ".html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#Get Book title and drop subtitle (:)
Title = soup.find("div", class_ = 'bookTitle').getText().replace("\n", "").split(":")[0]

# If a Div is a 'sectionHeading' then it is a h2 title (##)
# Else if a div is a 'noteText' then it is a quote (>)
qnt = 0
with open(str(Title + '.txt'), 'w') as f:
    for x in soup.find_all("div"):
        if soup.find_all("div")[qnt]['class'] == ['sectionHeading']:
            print("\n## " + soup.find_all("div")[qnt].getText().replace("\n",""), file=f)
        elif soup.find_all("div")[qnt]['class'] == ['noteText']:
            print("> " + soup.find_all("div")[qnt].getText().replace("\n","") + "\n", file=f)
        qnt = qnt+1
