#expect output in form
#libs = {id: [ordered_book_ids]}, [ordered_libs]

def gen_output(libs,order):
    with open("out.txt",'w') as out:
        out.write("{}\n".format(len(order)))
        for lib_id in order:
            book_list = libs[lib_id]
            out.write("{} {}\n".format(lib_id,len(book_list)))
            out.write(" ".join([str(b) for b in book_list])+"\n")

if __name__=="__main__":
    libs = {0: [5,2,587,6], 1:[3,4,5]} #test content
    order = [1,0]
    gen_output(libs, order)
