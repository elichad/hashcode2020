from structures import Library;

def get_data(filename="input.txt"):

    with open(filename, 'r') as f:
        lines = (f.readlines())
        # lines = lines.split()
        
        first_line = str(lines[0])
        first_line = first_line.split()
        # print(first_line)

        total_books = int(first_line[0])
        total_libs = int(first_line[1])
        total_days = int(first_line[2])

        print(total_books,total_libs,total_days)

        book_scores = str(lines[1])
        book_scores = book_scores.split()
  
        # print(book_scores)

        book_id_dict = {}

        for book in range(0,total_books):
            print(book, book_scores[book])
            # book_id = book
            # book_score = book_scores[book]
            # book_id_dict[book_id]=book_score

    #     print(type(lines))
        # print(book_id_dict)

    # del lines[0:2]

    # libraries = lines
    
    # library_dict = {}
    
    # for 

    

    # return(total_books,total_libs,total_days,book_id_dict)


get_data('a_example.txt')