def get_data(filename="input.txt"):

    with open(filename, 'r') as f:
        lines = (f.readlines())
        # lines = lines.split()

        total_books = int(lines[0][0])
        total_libs = int(lines[0][2])
        total_days = int(lines[0][4])

        # print(total_books,total_libs,total_days)

        book_scores = lines[1]
        book_scores = book_scores.split()
  
        book_id_dict = {}

        for book in range(0,total_books):
            # print(book, book_scores[book])
            book_id = book
            book_score = book_scores[book]
            book_id_dict[book_id]=book_score

        print(type(lines))
        #print(book_id_dict)

    

    return(total_books,total_libs,total_days,book_id_dict)


get_data('a_example.txt')