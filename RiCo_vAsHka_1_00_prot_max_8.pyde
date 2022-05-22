#mouseClicked
u=[]
i=[]
r=100
g=100
b=100
y=200
x=400
x=1
y=2
ctirat=3
def setup():
    size(1000,800)
    strokeWeight(10)
    background(255)
def draw():
    global bg,u,i
    background(r,g,b)
    fill(255)
    rect(250,150,100,50)
    if mousePressed==True:#
      if  mouseButton==LEFT:#
        u.append(mouseY)
        i.append(mouseX)
      elif mouseButton==RIGHT and (len(u))>0:#
          del u[len(u)-1]#
          del i[len(i)-1]#
    if len(u)>0:
        for index in range(len (u)):
            point(i[index],u[index])
        
     
def mouseClicked():
    global r,g,b
    if mouseX>250 and mouseX<350 and mouseY>150 and mouseY<200:
        text(u"цвет фона",700,350)
        r =random(0,255)
        g =random(0,255)
        b =random(0,255)
    if mouseX>250 and mouseX<350 and mouseY>150 and mouseY<200:
        text(u"цвет фона",700,350)
        r =random(0,255)
        g =random(0,255)
        b =random(0,255)
    global x,y,i,u
    
    if mouseButton==RIGHT:
        stroke(random(0,255),random(0,255),random(0,255))
    if mouseButton==CENTER:
        strokeWeight(random(0,255))
    if key=="c":
        background(255)
    if key=="r" and  mouseButton==LEFT:
        u.append(mouseY)
        i.append(mouseX)
        rect(mouseX,mouseY)
        

        
        
        
        
        
        
        
        
