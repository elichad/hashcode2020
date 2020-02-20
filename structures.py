from collections import OrderedDict

class Book: #unused?
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Library:
    def __init__(self, id, n_books, signup, scans, books):
        self.id = id
        self.n_books = n_books
        self.signup = signup
        self.scans = scans
        self.books = books #dict {id: score}

    def get_total_score(self):
        tot = 0
        for id in self.books.keys():
            tot += self.books[id]
        return tot

    def get_todays_books(self,all_scanned):
        ids = OrderedDict()
        while len(ids) < self.scans and len(self.books.keys())>0:
            best_id = max(self.books.keys(), key=lambda k: self.books[k])
            if best_id not in all_scanned:
                ids[best_id] = self.id
            del self.books[best_id] #always delete
        return ids
        #after this in main code: want all_scanned.add(ids)

    def get_ordered_books(self):
        s = sorted(self.books.keys(), key=lambda k: self.books[k])
        s.reverse()
        return s

        
#dict((k, bigdict[k]) for k in ('l', 'm', 'n'))
#initialise with : Library.books = dict((k, all_books[k] for k in lib_book_ids))    



if __name__=="__main__":
    books = {0: 10,1:20}
    libs = {0: Library(0,2,1,2,{0:10,1:20})}
    scanned = set()
    for lib_id in libs:
        lib = libs[lib_id]
        print(lib_id, lib.get_ordered_books(), lib.get_total_score(), lib.get_todays_books(scanned), lib.get_total_score()) #very well written test: 0 30 {0,1} 0 (but book 1 is scanned before 0)

