------------------------------------------------------------------------------------------------------------
📝 WEB HEADLINE SCRAPER
------------------------------------------------------------------------------------------------------------
This is a beginner-friendly web scraping project made using Python. 
It runs in the command line and pulls the latest headlines from the BBC News website, saving them to a file.

⚙️ Features:
1.Fetches the live HTML of the BBC News homepage.
2.Filters all links to find actual news headlines.
3.Removes all duplicate headlines.
4.Saves the clean, numbered list to headlines.txt.

🧠 Concepts Used:
-External Libraries (requests, beautifulsoup4)
-Loops (for)
-Conditional statements (if)
-Sets (to automatically remove duplicates)
-File Handling (with open... to write the file)
-String Methods (.startswith(), .get_text())

🏗️ How it works:
-The script uses requests to download the website's HTML.
-BeautifulSoup is used to parse the HTML and find all links.
-It loops through all links, filtering them by text length and URL (e.g., must start with '/news/') to find real articles.
-The unique headlines are sorted and saved to headlines.txt.

This project helped me practice using external libraries, parsing HTML, and handling real-world, messy web data.

Made by Aarya Manchanda
--------------------------------------------------------------------------------------------------------------