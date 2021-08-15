# KindleNotebook2Notion.py
![Preview](https://github.com/allanmviana/KindleNotebook2Notion.py/blob/main/img/img1%20-%20from%20to.png)

## How it works
Everytime you read a book from amazon ou send a document thru email to kindle, you can open it with your app too.
This way, you may open the book whithin the app and then share your notes.

![Export Highlights](https://github.com/allanmviana/KindleNotebook2Notion.py/blob/main/img/img2%20share.png)

This process will generate a `.html` file. 
Then, the `KindleNotebook2Notion.py` read this file and generates a `book title.txt` file following 2 simples rules:
- Chapters names are in `h2` style
- Highlights and notes are in quote `> ` style

From this .txt file, you can easily copy and paste in Notion
