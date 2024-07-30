class Article:
    all = []
    test_dict = {"author":"", 
                 "magazine":"", 
                 "title":""}
    
    authors = []
    articles = []
    magazines = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property ## AUTHOR ###############################################################
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        global authors
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
    articles_arr = []
    
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
        for articles in Article.all:
                if articles["author"] == self.name:
                    self.articles_arr.append(articles)
                return self.articles_arr
        
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

joe = Author("Joe")
vogue = Magazine("Vogue", "Fashion")
arttitle = "50 Ways to Not Pay Taxes"
article00 = (joe, vogue, arttitle)

moe = Author("Moe")
wsj = Magazine("WSJ", "Business")
arttitle2 = "100 Ways to go to Prison for Free"
article01 = (moe, wsj, arttitle2) 