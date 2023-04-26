from os import read, write

def readline():
  index = 0
  line = ""
  buffer = read(0,100)      #Buffer read limit is set to 100 characters
  string = buffer.decode()  #Decode makes the string more interpretable
  
  while index < len(string):
    current_char = string[index]
    if current_char == '\n':
      return line
    line += current_char
    index += 1
    
    if index == 100:
      buffer = read(0,100)
      string = buffer.decode()
      index = 0
      
  return "" #End of File reached
