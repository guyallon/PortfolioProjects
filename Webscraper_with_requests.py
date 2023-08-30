"""
This is an example of a web scraper script using requests library to scrape job posting comments from Hacker News (Ask HN) posted in June 2023.
After scraping and using BeautifulSoup to create a list of comments, the question: "Which programming language mentioned the most on job posts in June 2023?" , is being asked and
the script uses matplotlib library to generate a bar chart presenting the # of mentions per language.

This script can readily adjusted to scrape from different sites and/or search for other form of analytics within the text or other content.

"""

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
 
def main():
    url = "https://news.ycombinator.com/item?id=36152014"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]

#After scraping all comments from the url and saving them into a list,
# a keywords dict of programming languages is initiated.
    keywords = {
        "python": 0,
        "javascript": 0,
        "typescript": 0,
        "ruby": 0,
        "java": 0,
        "rust": 0,
        "c#": 0,
    }

    print(f"Elements: {len(elements)}")
    #A loop for iterating over each comment making it a list of words (alphabetical chars only) 
    for comment in comments:
        comment_text = comment.get_text().lower()
        words = comment_text.split(" ")
        words = {w.strip(".,/:;!@") for w in words}
       
    #A loop iterating each keyword in keywords and checking if this word appears in the comment 
        for k in keywords:
            if k in words:
                keywords[k] += 1
    print(keywords)

#Using matplotlib to create a bar chart showing the occurance of
#each programming language in these recent job posting data.
    

    plt.figure(figsize=(10, 6))  # Adjust the figure size for better aesthetics
    bars = plt.bar(keywords.keys(), keywords.values(), color='dodgerblue')
    plt.xlabel("Programming Language", fontsize=14)
    plt.ylabel("# of Mentions", fontsize=14)
    plt.title("Programming Language Mentions", fontsize=16)

    # Adding a grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Customizing the tick labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)

    # Adding a legend (if necessary)
    # plt.legend()

    # Adding some extra space for the x-axis labels
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()