import turtle
import time

t1, t2, t3, t4, t5, t6=turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
t_list=[t1, t2, t3, t4, t5, t6]
coord_dict={t1:(-250, 50), t2:(-175, 50), t3:(-50, 50), t4:(25, 50), t5:(150, 50), t6:(225, 50)}
for i in t_list:
  i.ht()
  i.speed(speed=0)
  i.pu()
  i.goto(coord_dict[i])
  i.pd()
turtle.ht()
dist=15
turtle.speed(speed=0)
turtle.pu()
turtle.goto(-95, 35)
turtle.pd()
for i in range(15):
  for j in range(4):
    turtle.fd(dist)
    turtle.rt(90)
  turtle.rt(45)
  turtle.fd(1)
  turtle.lt(45)
  dist-=1
dist=15
turtle.pu()
turtle.goto(-95, -20)
turtle.pd()
for i in range(15):
  for j in range(4):
    turtle.fd(dist)
    turtle.rt(90)
  turtle.rt(45)
  turtle.fd(1)
  turtle.lt(45)
  dist-=1
dist=15
turtle.pu()
turtle.goto(105, 35)
turtle.pd()
for i in range(15):
  for j in range(4):
    turtle.fd(dist)
    turtle.rt(90)
  turtle.rt(45)
  turtle.fd(1)
  turtle.lt(45)
  dist-=1
dist=15
turtle.pu()
turtle.goto(105, -20)
turtle.pd()
for i in range(15):
  for j in range(4):
    turtle.fd(dist)
    turtle.rt(90)
  turtle.rt(45)
  turtle.fd(1)
  turtle.lt(45)
  dist-=1

def draw_1(turt):
  global coord_dict
  turt.clear()
  turt.rt(90)
  turt.fd(100)
  turt.lt(90)
  turt.goto(coord_dict[turt])

def draw_2(turt):
  global coord_dict
  turt.clear()
  for i in range(3):
    turt.fd(50)
    turt.rt(90)
  turt.bk(50)
  turt.rt(90)
  turt.fd(50)
  turt.pu()
  turt.goto(coord_dict[turt])
  turt.pd()

def draw_3(turt):
  global coord_dict
  turt.clear()
  for i in range(3):
    turt.fd(50)
    turt.rt(90)
  turt.rt(90)
  for i in range(3):
    turt.fd(50)
    turt.rt(90)
  turt.pu()
  turt.rt(90)
  turt.goto(coord_dict[turt])
  turt.pd()

def draw_4(turt):
  global coord_dict
  turt.clear()
  for i in range(3):
    turt.lt(90)
    turt.bk(50)
  turt.lt(180)
  turt.bk(100)
  turt.pu()
  turt.rt(90)
  turt.goto(coord_dict[turt])
  turt.pd()

def draw_5(turt):
  global coord_dict
  turt.clear()
  turt.pu()
  turt.fd(50)
  turt.rt(180)
  turt.pd()
  for i in range(3):
    turt.fd(50)
    turt.lt(90)
  turt.bk(50)
  turt.rt(90)
  turt.bk(50)
  turt.pu()
  turt.goto(coord_dict[turt])
  turt.pd()

def draw_6(turt):
  global coord_dict
  turt.clear()
  turt.pu()
  turt.fd(50)
  turt.rt(180)
  turt.pd()
  for i in range(2):
    turt.fd(50)
    turt.lt(90)
  for i in range(4):
    turt.fd(50)
    turt.rt(90)
  turt.goto(coord_dict[turt])

def draw_7(turt):
  global coord_dict
  turt.clear()
  turt.lt(180)
  turt.bk(50)
  turt.lt(-110)
  turt.bk(108.5)
  turt.pu()
  turt.lt(-70)
  turt.goto(coord_dict[turt])
  turt.pd()

def draw_8(turt):
  global coord_dict
  turt.clear()
  for i in range(3):
    turt.fd(50)
    turt.rt(90)
  for i in range(4):
    turt.bk(50)
    turt.lt(90)
  turt.rt(90)
  turt.goto(coord_dict[turt])

def draw_9(turt):
  global coord_dict
  turt.clear()
  for i in range(5):
    turt.fd(50)
    turt.rt(90)
  turt.fd(100)
  turt.lt(90)
  turt.bk(50)
  turt.pu()
  turt.goto(coord_dict[turt])
  turt.pd()

def draw_0(turt):
  global coord_dict
  turt.clear()
  for i in range(2):
    turt.fd(50)
    turt.rt(90)
    turt.fd(100)
    turt.rt(90)
  turt.fd(50)
  turt.rt(117)
  turt.fd(111)
  turt.lt(117)
  turt.goto(coord_dict[turt])

def draw(num, turt):
  if num==0:
    draw_0(turt)
  elif num==1:
    draw_1(turt)
  elif num==2:
    draw_2(turt)
  elif num==3:
    draw_3(turt)
  elif num==4:
    draw_4(turt)
  elif num==5:
    draw_5(turt)
  elif num==6:
    draw_6(turt)
  elif num==7:
    draw_7(turt)
  elif num==8:
    draw_8(turt)
  elif num==9:
    draw_9(turt)

def list_oper(l):
  for i in range(len(l)):
    if (log[-1][i]!=l[i]):
      if i==0:
        draw(l[i], t1)
      elif i==1:
        draw(l[i], t2)
      elif i==2:
        draw(l[i], t3)
      elif i==3:
        draw(l[i], t4)
      elif i==4:
        draw(l[i], t5)
      elif i==5:
        draw(l[i], t6)

b=(time.asctime())[11:19]
log=[]
start_time=[]
for i in b:
  try:
    start_time.append(int(i))
  except ValueError:
    continue
log.append(start_time)

for i in range(len(start_time)):
  if i==0:
    draw(start_time[i], t1)
  elif i==1:
    draw(start_time[i], t2)
  elif i==2:
    draw(start_time[i], t3)
  elif i==3:
    draw(start_time[i], t4)
  elif i==4:
    draw(start_time[i], t5)
  elif i==5:
    draw(start_time[i], t6)

while True:
  a=(time.asctime())[11:19]
  now_time=[]
  for i in a:
    try:
      now_time.append(int(i))
    except ValueError:
      continue
  list_oper(now_time)
  log.append(now_time)
  if len(log)>10:
     log.pop(0)