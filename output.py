#expect output in form
#libs = {id: [ordered_book_ids]}, [ordered_libs]

def gen_output(libs,order):
    with open("out.txt") as out:
        out.write(len(order)+"\n")
        for lib_id in order:
            book_list = libs[lib_id]
            out.write(lib_id+" "+len(book_list)"\n")
            out.write(" ".join(book_list)+"\n")

