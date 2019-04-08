list_= []
with open ("proband.csv") as f :
   for i in f:
      a = i.strip('\n')  # delete the \n in each line
      list_.append(a)
with open("1MV1.csv") as read_file, open("out.csv","w") as out_file:
   header = next(read_file)
   out_file.write(header)
   for read_line in read_file:
      if any ([read_line.startswith(id) for id in list_]):
         out_file.write(read_line)
