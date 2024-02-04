#!/usr/bin/env python3
import sys
sys.path.append('lib') 
import ipdb

from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
   

    author1 = Author("Wairimu Mwaura")
    author2 = Author("Tasha Wangari")
    
    ipdb.set_trace()
    
    magazine1 = Magazine("Story Hot", "True love")
    magazine2 = Magazine("Spice FM", "Entertainment")

   
    ipdb.set_trace()

    article1 = author1.add_article(magazine1, "First Magazine")
    article2 = author2.add_article(magazine1, "The Trending One")
    article3 = author1.add_article(magazine2, "Truly True")

    
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")

    # DO NOT REMOVE THIS
    ipdb.set_trace()
