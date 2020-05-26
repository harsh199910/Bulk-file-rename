

import os

def main():
   i = 0
   path="path/"
   for filename in os.listdir(path):
      my_dest ="example " + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      os.rename(my_source, my_dest)
      i += 1

main()
