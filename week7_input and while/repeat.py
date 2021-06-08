promt = "\n tell me something"
promt += "\nwrite exit to end:"
message = ""
active = True
while active:
  message = input(promt)
  if message == 'exit':
    active = False
  else:
    continue