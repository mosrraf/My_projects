import Tools
Tools.clear()
text=Tools.base()
ans=Tools.In("do you want to start? (yes/no)\nans: ",["yes","no"])
while ans=="yes":
  Tools.clear()
  size=Tools.size()
  text=Tools.base()
  array=Tools.opentolist("system")
  choice=int(Tools.In(text+"\nyour choice: ",[str(i) for i in range(1,size+1)]))
  choice-=1
  if array[choice]=="New":
    Tools.add_groups()
  elif array[choice]=="Add":
    Tools.addcontent()
  elif array[choice]=="Random":
    Tools.get()
  elif array[choice]=="Delete":
    Tools.delete()
  elif array[choice]=="Replace":
    Tools.replace()
  elif array[choice]=="Show":
    text=Tools.show()
    print(text)
    input("press enter to continue.\n")
  elif array[choice]=="Search":
    Tools.search()
  elif array[choice]=="Add command":
    Tools.addcontent("system")
  elif array[choice]=="Exit":
    print ("see you later")
    ans="no"
  elif array[choice]=="Pick my day":
    Tools.pickday()
  elif array[choice]=="Change order":
    Tools.exchangeorder()
  elif array[choice]=="remove":
    Tools.rm()
Tools.clear()
  
