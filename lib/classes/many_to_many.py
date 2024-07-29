class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            print("Must be a valid author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            print("Must be a valid magazine")

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, 'title'):
            self._title = title
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
        def __init__(self, author, magazine, title):
            self.author = author
            self.magazine = magazine
            self.title = title

        @property
        def author(self):
            return self._author
        

    
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
article00 = (joe, vogue, "50 Ways to Not Pay Taxes")