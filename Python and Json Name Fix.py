import os


#A little Python app that I wrote to quickly rename a bunch of Python and Json files in a directory, stripping my initials from the end of a filename. 
#This saved me almost an hour's worth of work as there was a lot of files to rename.

def main():
  for filename in os.listdir("."):
    if filename.endswith("JG.py"):
      f3 = filename[:7]+".py"
      os.rename(filename, f3)
    if filename.endswith("JG.json"):
      f2 = filename[:7]+".json"
      os.rename(filename, f2)
      
	  
	  
main()