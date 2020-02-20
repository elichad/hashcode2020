from structures import Library;

def get_data(filename="input.txt"):

    with open(filename, 'r') as f:
        lines = (f.readlines())
        # lines = lines.split()
        
        first_line = str(lines[0])
        first_line = first_line.split()
        # print(first_line)

        total_books = int(first_line[0])
        total_libraries = int(first_line[1])
        total_days = int(first_line[2])

        # print(total_books,total_libs,total_days)

        book_scores = str(lines[1])
        book_scores = book_scores.split()
  
        # print(book_scores)

        book_id_dict = {}

        for book in range(0,total_books):
            # print(book, book_scores[book])
            book_id = book
            book_score = book_scores[book]
            book_id_dict[int(book_id)]=int(book_score)

        #  print(type(lines))
        # print(book_id_dict)

    del lines[0:2]

    libraries = lines
    # print(libraries)
    list_libraries = []

    for library in range(0, len(libraries), 2):
        # print(library)

        library_info = str(libraries[library])
        library_info = library_info.split()

        num_books_in_lib = library_info[0]
        signup_process_days = library_info[1]
        books_per_day = library_info[2]
    
        books_in_lib = str(libraries[library+1])
        books_in_lib = books_in_lib.split()
        # print(books_in_lib)
        # print("length",len(books_in_lib))

        book_lib_dict = {}

        for book in range(0,len(books_in_lib)):
            book_id = book
            # print(book_id)
            # print(books_in_lib[book])
            book_score = books_in_lib[book]
            book_lib_dict[int(book_id)]=int(book_score)
        library_id = library/2
        # print(book_lib_dict)
        library_obj = Library(int(library_id), int(num_books_in_lib),int(signup_process_days), int(books_per_day), book_lib_dict )
        list_libraries.append(library_obj)
    # print(list_libraries)
    return(int(total_books),int(total_libraries),int(total_days),book_id_dict, list_libraries)


get_data('a_example.txt')