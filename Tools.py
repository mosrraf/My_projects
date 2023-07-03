from datetime import datetime
import os
import random 
def rm(arg=None):
  clear()
  if arg==None:
    ans=In("do you want to remove a list? (yes/no) \nans: ",["yes","no"])
  else:
    ans="yes"
  while ans=="yes":
   clear()
   if arg==None:
     text=show("groups")
     collection=opentolist("groups")
     choice=int(In(text+"enter the choice:\n",[str(i) for i in range(1,len(collection)+1)]))
     name=collection [choice-1]
     collection.remove(collection [choice-1])
     command='rm '+name+'.txt'
     os.system(command)
     command='rm groups.txt'
     os.system(command)
     for name in collection:
       add(name,"groups")
     print(show("groups"))
     ans=In("do you want to do it again? (yes/no) \nans: ",["yes","no"])
   else:
     name=arg
     command='rm '+name+'.txt'
     os.system(command)
     ans="no"
   
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
    text=show("groups")
    choice=int(In(text+"please, enter your choice:\n", [str(i)for i in range (1,len(collection)+1)]))
    return collection[choice-1]
  except:#if there are no groups tell me and return a value to check upon it
    print("there are no groups\nadd groups through option new and then come back.")
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
        text+=f"({index}) {name}.\n\n"
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
      collection=opentolist(group)
      choice=int(In(text+"enter the choice:\n",[str(i) for i in range(1,len(collection)+1)]))
      exchange=input("enter the replacement:\n")
      collection [choice-1]=exchange
      rm(group)
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
      collection=opentolist(group)
      choice=int(In(text+"please enter your choice:\n",[str(i) for i in range(1,len(collection)+1)]))
      collection.remove(collection[choice-1])
      rm(group)
      for text in collection:
        if text==',':
          continue 
        add(text,group)
      ans=In("do you want to delete another item? (yes/no) \nans: ",["yes","no"])
      if ans=="no":
        return 1
    except:
      print("there is no such file.")
      return 0
  return 0
def addcontent(arg=None,star=None):#used to add content to certain groups.
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
    name=""
    if group=="dates":
      return 0
    if arg==None or arg=="groups":
      name+=input("enter the name:\n")
    elif arg=="videos":
      collection=opentolist("stars")
      if star==None:
        star=input("please enter star's name: ")
        result=search("stars",star)
        if result==1:
          add(star,'stars')
        else:
          choice=int(In(result[-1]+"please,enter your choice:",[str(i) for i in result[:-1]]))
          star=collection [choice-1]
      clear()
      reply=In("is there another stars?(yes/no)\nans: ",["yes","no"])
      video=star+" "
      while reply=="yes":
        clear()
        name=input("please enter star's name: ")
        result=search("stars",name)
        if result==1:
          add(name,"stars")
          collection=opentolist("stars")
          video+=collection[-1]+" "
        else:
          choice=int(In(result[-1]+"please,enter your choice:",[str(i) for i in result[:-1]]))
          clear()
          video+=collection[choice-1]+" "
        reply=In("is there another stars?(yes/no)\nans: ",["yes","no"])
      clear()
      reply=In("does the video has a name?(yes/no)\nans: ",["yes","no"])
      clear()
      if reply=="yes":
        video_name=input("please, enter video's name: ")
        video+=f"[{video_name}] "
        clear()
      video+=input("please, enter duration: ")
      clear()
      name=video
      input("the inputted video: "+name+"\npress enter to continue.")
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
    star=None
  return ans
def add_groups():#add groups that i create
  clear()
  ans=In("Do you want to add to new group? (yes/no)\nans: ",["yes","no"])
  while ans=="yes":
    clear()
    ans=addcontent("groups")
def search(arg=None,name=None):#used in content search
  clear()
  if arg==None:
    ans=In("do you want to search for a name ? (yes/no) \nans: ",["yes","no"])
  else:
    ans="yes"
  if ans=="yes" and arg==None:
    group =groups()
    if group==0:#if no groups terminate
      return 0
    clear()
  elif arg!=None and ans=="yes":
    group=arg
  while ans=="yes":
    clear()
    existence=False#assumption of mission failure 
    try:
      with open(group+'.txt', 'r') as file:
        content = file.read()
        file.close()
      collection=content.split(',')
      collection.remove("")
      found=[]
      txt=""
      if name==None:
        name=input("please enter the name:\n")
      for item in collection:
        if name in item:
          if arg==None:
            print(f"({collection.index(item)+1}) {item}.")
          elif arg=="stars":
            txt+=f"({collection.index(item)+1}) {item}.\n"
            found.append(collection.index(item)+1)
            existence=True#mission succeeded
      found.append(txt)
      if arg=="stars" and existence:
        return found
      if not existence:#if still failure tell me
        print("not existed!")
        if arg!=None:
          return 1
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
  text=f"\nsearch by: {choosen(dur)}  {choosen(cat)} {choosen(date)}"
  return text
def get_video():#gets a random order to video 
  ans=In("do you have multi videos and want to pick one? (yes/no)\nans: ",["yes","no"])
  if ans=="yes":
    clear()
    numberofvideos=int(In("please enter number of videos:\n",[str(i) for i in range(1,1000)]))
    print(choosen([i for i in range (1,numberofvideos+1)]))
def get_from_groups():#random dates for groups and then get a video 
  clear()
  ans=In("do you want to get a random video from groups? (yes/no)\nans: ",["yes","no"])
  if ans=="yes":
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
      counter=1
      while ans=="yes":
        clear()
        dates=days(day,month,year)
        print("date: ",choosen(dates))
        input("press enter to continue. ")
        clear()
        respond=In("did you find video to add? (yes/no)\nans: ",["yes","no"])
        if respond=="yes":
          clear()
          addcontent("videos")
          break
        else:
          counter+=1
          if counter>3:
            break
          else:
            continue
        clear()
      ans=In("do you want to repeat? (yes/no)\nans: ",["yes","no"])
    clear()
def get(group=None):#picks randomly from groups
  clear()
  if group==None:
    ans=In("do you want to pick randomly? (yes/no) \nans: ",["yes","no"])
    clear()
  else:
    ans="yes"
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
      else:
        collection=opentolist(group)
        choice=choosen(collection)
        if group=="groups":
          group=choice
          continue 
        print(choice)
        if group=="stars":
          print(duration())
          get_video()
          clear()
          respond=In("did you find video to add? (yes/no)\nans: ",["yes","no"])
          if respond=="yes":
            addcontent("videos",choice)
          clear()
      ans=In("do you want to get another one? (yes/no) \nans: ",["yes","no"])
      clear()
    ans=In("do you want to random again? (yes/no) \nans: ",["yes","no"])
    if ans=="yes":
      get("groups")
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
  collection=opentolist("today")
  clear()
  if collection==1:
    ans=In("do you want to pick your day? (yes/no) \nans: ",["yes","no"])
  elif collection [0]==str(datetime.today()).split(" ")[0]:
    print(show("today"))
    input("press enter to continue.\n")
    ans="no"
  else:
    ans=In("do you want to pick your day? (yes/no) \nans: ",["yes","no"])
    clearlist("today")
  try:
    while ans=="yes":
      clear()
      file=open("groups.txt")
      content=file.read()
      file.close()
      collection=content.split(',')
      collection.remove("")
      result=str(datetime.today()).split(" ")[0]+','
      for item in collection:
        if item in ["dates","groups"]:
          continue
        if datetime.today().strftime("%A") not in ["Friday","Tuesday"] and item=="movies":
          continue 
        file=open(item+".txt")
        content=file.read()
        file.close()
        array=content.split(',')
        array.remove("")
        if item=="videos":
          selected=choosen(array)
          minutes=selected.split(" ")[-1].split(":")
          if len(minutes)<3:
            if int(minutes[0])<40:
              selected+="\n"+choosen(array)
          result+=item+": "+selected+","
        elif item=="stars":
          result+=item+": "+choosen(array)+duration()+','
        else:
          result+=item+": "+choosen(array)+","
      result=result[:-1]
      add(result,"today")
      print(show("today"))
      ans=In("do you accept result? (yes/no) \nans: ",["yes","no"])
      if ans=="yes":
        ans="no"
      else:
        ans="yes"
        clearlist("today")
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
    print(f"{name} is not existed.\n")
    return 1
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
def clearlist(group):
  with open(group+'.txt', 'r+') as file:
    content = file.read()
    file.truncate(0)#delete file conrents
  file.close()
