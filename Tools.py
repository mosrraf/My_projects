from datetime import datetime
import os
import random 
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
def In(text="please, enter:",valid=None):# check if the entered value is within the valid values
	if valid ==None:
	  print("missing argument!\nIn(text,valid)\n                ^")
	else:
	  x=input(text).lower()
	  while x not in valid:
	    clear()
	    x=input("invalid value!\nplease try again: \n"+text).lower()
	  return x
def add(value,name):#adds texts to files
  try:
    with open(name+'.txt', 'r') as file:
      content = file.read()
    collection=content.split(',')
    collection.remove("")
    file.close()
    file=open (name+".txt","a")
    if ',' in value:#for multi text texts
      names=value.split(',')
      for name in names:
        if name not in collection:
          file.write(name+",")
        else:
          print(f"{name} is already existed!")
    else:#for single text texts
      if value not in collection:
        file.write(value+",")
      if value in collection:
        print(f"{value} is already existed!")
  except:
    file=open(name+".txt",'w')#if there is no file create a one and then add the text to it
    file.write(value+",")
  file.close()
def days(day_1,month_1,year_1):#generate dates from a certain date till today
  date=datetime.now()
  month=date.month
  day=date.day
  year=date.year
  dates=[]
  y,m,d=year_1,month_1,day_1
  while y<=year:
    max_day=30
    if m==2 and y%4==0:
      max_day=29
    if m==2 and y%4!=0:
      max_day=28
    if m in [1,3,5,7,8,10,12]:
      max_day=31
    if y<year:
      while d<=max_day:
        dates.append(f"{d}/{m}/{y}")
        d+=1
      if m!=12:
        d=1
        m+=1
      else:
        d=1
        m=1
        y+=1
    else:
      if m<month:
        while d<=max_day:
          dates.append(f"{d}/{m}/{y}")
          d+=1
        d=1
        m+=1
      if m==month:
        while d<=day:
         dates.append(f"{d}/{m}/{y}")
         d+=1
        break
  return dates
def groups():#opens file called groups contains groups we created and asks to pick a one
  try:
    clear()
    file=open ("groups.txt")
    content = file.read()
    file=file.close()
    collection=content.split(',')
    collection.remove("")
    index=1
    text=""
    for name in collection:
      text+=f"({index}) {name}.\n"
      index+=1
    choice=int(In(text+"please, enter your choice:\n", [str(i)for i in range (1,len(collection)+1)]))
    return collection[choice-1]
  except:#if there are no groups tell me and return a value to check upon it
    print("there are no groups\nadd groups through option add and then come back.")
    return 0
def show(arg=None):#opens file and show its content
  clear()
  if arg==None:
    ans=In("do you want to show content ? (yes/no) \nans: ",["yes","no"])
  else:
    ans="yes"
  if ans=="yes":
    clear()
    if arg==None:
      group =groups()
      if group==0:#if there are no groups terminate
        return 0
      clear()
    else:
      group=arg
    try:
      file=open (group+".txt")
      content = file.read()
      file=file.close()
      collection=content.split(',')
      collection.remove("")
      index=1
      text=""
      for name in collection:
        text+=f"({index}) {name}.\n"
        index+=1
      return text#return contents in certain style 
    except:#if file is empty or not there
      if arg==None:
        print("file does not exist.")
        input("press enter to continue.")
      return 0
def replace():#replaces a single value at a time
  clear()
  ans=In("do you want to replace names? (yes/no)\nans: ",["yes","no"])
  if ans=="yes":
    group =groups()
    if group==0:#if there are no groups terminate
      ans="no"
    clear()
  while ans=="yes":
    clear()
    text=show(group)#show choices
    try:
      with open(group+'.txt', 'r+') as file:
        content = file.read()
        file.truncate(0)
        file.close()
      collection=content.split(',')
      collection.remove("")
      choice=int(In(text+"enter the choice:\n",[str(i) for i in range(1,len(collection)+1)]))
      exchange=input("enter the replacement:\n")
      collection [choice-1]=exchange
      for text in collection:
        if text==',':
          continue 
        add(text,group)
      clear()
      ans=In(f"do you want to replace another {group}? (yes/no) \nans: ",["yes","no"])
    except:#if group is empty terminate
      print (f"no items to replace.\nhint: add to {group} then come back again")
      ans="no"
def delete (arg=None):#delete items from files
  clear()
  ans=In("do you want to delete name? (yes/no) \nans: ",["yes","no"])
  while ans=="yes":
    clear()
    if arg==None:
      group =groups()
      if group==0:#terminate when there are no groups
        return 0
      clear()
    else:
      group=arg
    text=show(group)
    try:
      with open(group+'.txt', 'r+') as file:
        content = file.read()
        file.truncate(0)#delete file conrents
      collection=content.split(',')
      collection.remove("")
      choice=int(In(text+"please enter your choice:\n",[str(i) for i in range(1,len(collection)+1)]))
      collection.remove(collection[choice-1])
      for text in collection:
        if text==',':
          continue 
        add(text,group)
      ans=In("do you want to delete another item? (yes/no) \nans: ",["yes","no"])
      if ans=="no":
        return 1
      return 0
    except:
      print("there is no such file.")
      return 0
def addcontent(arg=None):#used to add content to certain groups.
  clear()
  if arg==None:
    ans=In("do you want to add content? (yes/no)\nans: ",["yes","no"])
    if ans=="yes": 
      group =groups()
      if group==0:#if no groups terminate.
        ans="no"
      clear()
  else:
    ans="yes"
    group=arg
  while ans=="yes":
    clear()
    if group=="dates":
      return 0
    name=input("enter the name:\n")
    add(name,group)
    clear()
    ans=In("do you want to edit input submitted? (yes/no)\nans: ",["yes","no"])
    clear()
    if ans=="yes":
      if delete(group)==1:
        clear()
        text=show(group)
        print(text)
        input("press enter to continue.\n")
      clear()
    ans=In("do you want to add another one? (yes/no) \nans: ",["yes","no"])
    return ans
def add_groups():#add groups that i create
  clear()
  ans=In("Do you want to add to new group? (yes/no)\nans: ",["yes","no"])
  while ans=="yes":
    clear()
    ans=addcontent("groups")
def search():#used in content search
  clear()
  ans=In("do you want to search for a name ? (yes/no) \nans: ",["yes","no"])
  if ans=="yes":
    group =groups()
    if group==0:#if no groups terminate
      return 0
    clear()
  while ans=="yes":
    clear()
    existence=False#assumption of mission failure 
    try:
      with open(group+'.txt', 'r') as file:
        content = file.read()
        file.close()
      collection=content.split(',')
      collection.remove("")
      name=input("please enter the name:\n")
      for item in collection:
        if name in item:
          print(f"({collection.index(item)+1}) {item}.")
          existence=True#mission succeeded
      if not existence:#if still failure tell me
        print("not existed!")
      ans=In("do you want to search again ? (yes/no) \nans: ",["yes","no"])
    except:
      print ("no file to search.\nhint: add content then come back again")
      ans="no"
def choosen(array):
   ten_chosen=[random.choice(array) for i in range(0,10)]
   return random.choice(ten_chosen)
def duration ():#gets random video duration 
  minutes=100
  dur=[i for i in range (0, minutes+1)]
  dur.append("open duration")
  cat=["relevance","duration","date"]
  date=["day","week","month","year","any"]
  print(f"search by: {choosen(dur)} , {choosen(cat)}, {choosen(date)}.")
def get_video():#gets a random order to video 
  ans=In("do you have multi videos and want to pick one? (yes/no)\nans: ",["yes","no"])
  if ans=="yes":
    clear()
    numberofvideos=int(In("please enter number of videos:\n",[str(i) for i in range(1,100)]))
    print(choosen([i for i in range (1,numberofvideos+1)]))
  input("press enter to continue.\n")
def get_from_groups():#random dates for groups and then get a video 
  clear()
  ans=In("do you want to get a random video from groups? (yes/no)\nans: ",["yes","no"])
  if ans==yes:
    numberofgroups=int(In("please enter number of groups:\n",[str(i) for i in range(1,100)]))
    while ans=="yes":
      clear()
      print(choosen([i for i in range (1,numberofgroups+1)]))
      input("press enter to continue.")
      clear()
      day=int(In("please enter a day: ",[str(i) for i in range(1,32)]))
      clear()
      month=int(In("please enter a month: ",[str(i) for i in range(1,13)]))
      clear()
      year=int(In("please enter a year: ",[str(i) for i in range(2011,datetime.now().year+1)]))
      clear()
      while ans=="yes":
        clear()
        dates=days(day,month,year)
        print(choosen(dates))
        get_video()
        clear()
        ans=In("do you want to repeat same? (yes/no)\nans: ",["yes","no"])
        clear()
      ans=In("do you want to repeat? (yes/no)\nans: ",["yes","no"])
    clear()
def get():#picks randomly from groups
  clear()
  ans=In("do you want to pick randomly? (yes/no) \nans: ",["yes","no"])
  if ans=="yes":
      respond=In("Do you want to pick from specific group? (yes/no)\nans: ",["yes","no"])
      if respond=="yes":#if yes pick your group 
        group =groups()
        if group==0:
          return 0
        clear()
      else:#if no you'll get it randomly.
        group="groups"
  try:
    while ans=="yes":
      clear()
      if group=="dates":
        get_from_groups()
        respond=In("did you find video to add? (yes/no)\nans: ",["yes","no"])
        if respond=="yes":
          addcontent("videos")
      else:
        with open(group+'.txt', 'r') as file:
          content = file.read()
        collection=content.split(',')
        collection.remove("")
        choice=choosen(collection)
        if group=="groups":
          group=choice
          continue 
        print(choice)
        if group=="stars":
          duration()
          get_video()
          respond=In("did you find video to add? (yes/no)\nans: ",["yes","no"])
          if respond=="yes":
            addcontent("videos")
          clear()
      ans=In("do you want to get another one? (yes/no) \nans: ",["yes","no"])
      if ans=="yes":
        group="groups"
  except:
    print ("add to your content first then come back")
def base():
  main_group="system"
  if show(main_group)==0:
    text="New,Add,Random,Delete,Replace,Show,Search,Add command,Exit"
    add(text,main_group)
    return base()
  else:
    return show(main_group)
def size():
  file=open ("system.txt")
  content = file.read()
  file=file.close()
  collection=content.split(',')
  collection.remove("")
  return len(collection)
def pickday ():
  clear()
  ans=In("do you want to pick your day? (yes/no) \nans: ",["yes","no"])
  try:
    while ans=="yes":
      clear()
      file=open("groups.txt")
      content=file.read()
      file.close()
      collection=content.split(',')
      collection.remove("")
      for item in collection:
        if item =="dates":
          continue
        if datetime.today().strftime("%A") not in ["Friday","Tuesday"] and item=="movies":
          continue 
        file=open(item+".txt")
        content=file.read()
        file.close()
        array=content.split(',')
        array.remove("")
        if item=="stars":
          print(item+": "+choosen(array))
          duration ()
          print("\n")
        else:
          print(item+": "+choosen(array)+"\n")
      ans=In("do you want to repeat? (yes/no) \nans: ",["yes","no"])
  except:
    print("you have no groups.")
def opentolist(name):
  try:
    file=open(name+".txt")
    content=file.read()
    file.close()
    collection=content.split(',')
    collection.remove("")
    return collection
  except:
    print("you have no groups.")
def exchangeorder():
  clear()
  try:
    ans=In("do you want exchange orders ? (yes/no) \nans: ",["yes","no"])
    while ans=="yes":
      text=show("system")
      with open('system.txt', 'r+') as file:
        content = file.read()
        file.truncate(0)#delete file conrents
      file.close()
      collection=content.split(',')
      collection.remove("")
      size=len(collection)
      first=int(In(text+"\nfirst one:",[str(i) for i in range(1,size+1)]))
      clear()
      second=int(In(text+"\nsecond one:",[str(i) for i in range(1,size+1)]))
      temp=collection[first-1]
      collection[first-1]=collection[second-1]
      collection[second-1]=temp
      for item in collection:
        if item==',':
          continue 
        add(item,"system")
      clear()
      text=show("system")
      print(text)
      ans=In("do you want to repeat? (yes/no) \nans: ",["yes","no"])
  except:
    print("you have no options.")