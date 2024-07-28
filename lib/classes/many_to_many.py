class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
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
        
        # @author.setter
        # def author(self, author):
        #     if isinstance(author, str) and len(author) > 0:
        #         self._author = author
        #         pass
    
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

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass