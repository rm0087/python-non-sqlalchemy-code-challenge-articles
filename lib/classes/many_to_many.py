class Article:
    all = []
    test_dict = {"author":"", 
                 "magazine":"", 
                 "title":""}
    
    authors = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property ## AUTHOR ###############################################################
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
            Article.test_dict["author"] = self.author.name
            if author.name not in Article.authors:
                Article.authors.append(author.name)
            else: pass
        else:
            print("Must be a valid author")
        
    @property ## MAGAZINE ###############################################################
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
            Article.test_dict["magazine"] = magazine.name

        else:
            print("Must be a valid magazine")

    @property ## TITLE ###############################################################
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, 'title'):
            self._title = title
            Article.test_dict["title"] = title
            Article.all.append(Article.test_dict.copy())
        else:
            print("Title must be a string between 5 and 50 characters")
        
        
class Author:
    
    
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, 'name'):
            self._name = name
        else:
            print("Author name must be a string with at least 1 character!")
            

    def articles(self):
        articles_arr = []
        for article in Article.all:
                if article["author"] == self.name:
                    articles_arr.append(article)
        return articles_arr
        
        def __init__(self, author, magazine, title):
            self.author = author
            self.magazine = magazine
            self.title = title

        # @property
        def author(self):
            pass
        

    
        def magazines(self):
            pass

        def add_article(self, magazine, title):
            pass

        def topic_areas(self):
            pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property #name
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <=  16:
            self._name = name
        else:
            print("Magazine name must be a string between 2 and 16 characters")

    @property #category
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) >0:
            self._category = category
        else:
            print("Magazine category must be a string that is at least 1 character")  
    
    
    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine = Magazine("Vogue", "Fashion")
article_1 = Article(author_1, magazine, "How to wear a tutu with style")
article_2 = Article(author_1, magazine, "Dating life in NYC")
article_3 = Article(author_2, magazine, "How to be single and happy")

# assert len(author_1.articles()) == 2
# assert len(author_2.articles()) == 1
# assert article_1 in author_1.articles()
# assert article_2 in author_1.articles()
# assert article_3 not in author_1.articles()
# assert article_3 in author_2.articles()