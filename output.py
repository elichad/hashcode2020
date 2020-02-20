#expect output in form
#libs = {id: [ordered_book_ids]}, [ordered_libs]
from collections import OrderedDict

def gen_output(libs):
    with open("out.txt",'w') as out:
        out.write("{}\n".format(len(libs.keys())))
        for lib_id in libs.keys():
            book_list = libs[lib_id]
            if len(book_list)==0:
                continue
            out.write("{} {}\n".format(lib_id,len(book_list)))
            out.write(" ".join([str(b) for b in book_list])+"\n")

if __name__=="__main__":
    libs = OrderedDict({0: [5,2,587,6], 1:[3,4,5]}) #test content
    gen_output(libs)
