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

i_add = 0
d_track = 0
libs_active = []
lib_adding = None
for d in range(0,tot_days):
  if d == d_track:
    if lib_adding:
      print("adding {} at day {}".format(i_add,d))
      libs_active.append(lib_adding)
    i_add+=1
    if i_add<len(sorted_libs):
      print("starting {} at day {}".format(i_add,d))
      lib_adding=sorted_libs[i_add]
      d_track = d + lib_adding.signup - 1

  for l in libs_active:
    bookos = l.get_todays_books(all_scanned)
    print("books for lib {} at day {}: {}".format(l.id,d,bookos))
    
    if l.id not in libs_to_books:
      libs_to_books[l.id] = []
    
    if len(bookos) > 0:
      for b in bookos:
        all_scanned.add(b)
        libs_to_books[l.id].append(b)

output.gen_output(libs_to_books)
