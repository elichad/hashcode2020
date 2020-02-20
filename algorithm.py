from collections import OrderedDict

import structures
import output
from hash_parser import get_data


""" libs = [structures.Library(0,2,1,2,{0:10,3:20})]
libs.append(structures.Library(1,1,0,2,{1:10000}))
libs.append(structures.Library(2,1,1,2,{2:40})) """

tot_books, tot_libs, tot_days, books, libs = get_data("a_example.txt")

all_scanned = set()
libs_to_books = OrderedDict()

def get_total_score(lib):
  print(lib.get_total_score())
  return lib.get_total_score()

sorted_libs = sorted(libs, key = lambda lib: ((lib.scans * lib.get_total_score()) - lib.signup))
sorted_libs.reverse()
for l in sorted_libs:
  print(l.id)
  bookos = l.get_ordered_books()
  after_books = []
  print("books: {}".format(bookos))
  for booko in bookos:
    if (booko not in all_scanned):
      all_scanned.add(booko)
      after_books.append(booko)
  
  if len(after_books) > 0:
    libs_to_books[l.id] = after_books

output.gen_output(libs_to_books)
