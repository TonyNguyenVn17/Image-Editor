from graphics import*
from Button import*
 
def brighten(cats): 
    for i in range(500):
        for j in range(451):
            image = cats.getPixel(i,j)
            r,g,b = image[0]+20,image[1]+20,image[2]+20
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            cats.setPixel(i,j,color_rgb(r,g,b))
           
 
def darken(cats):
    for i in range(500):
        for j in range(451):
            image = cats.getPixel(i,j)
            r,g,b = image[0]-20,image[1]-20,image[2]-20
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            cats.setPixel(i,j,color_rgb(r,g,b))
 
def blurr(cats):
    for i in range(498):
        for j in range(449):
            image1 = cats.getPixel(i,j)
            image2 = cats.getPixel(i,j+1)
            image3 = cats.getPixel(i,j+2)
            image4 = cats.getPixel(i+1,j)
            image5 = cats.getPixel(i+1,j+1)
            image6 = cats.getPixel(i+1,j+2)
            image7 = cats.getPixel(i+2,j)
            image8 = cats.getPixel(i+2,j+1)
            image9 = cats.getPixel(i+2,j+2)
           
 
            rave = (image1[0]+image2[0]+image3[0]+image4[0]+image5[0]+image6[0]+image7[0]+image8[0]+image9[0])//9
            gave = (image1[1]+image2[1]+image3[1]+image4[1]+image5[1]+image6[1]+image7[1]+image8[1]+image9[1])//9
            bave = (image1[2]+image2[2]+image3[2]+image4[2]+image5[2]+image6[2]+image7[2]+image8[2]+image9[2])//9
 
            cats.setPixel(i,j,color_rgb(rave,gave,bave))
 
 
def contrast(cats):
    for i in range(500):
        for j in range(451):
            color = []
            image = cats.getPixel(i,j)
            for k in range(3):
                if image[k]> 127:
                    image[k]+=20
                else:
                    image[k]-=20
                   
                if image[k] > 255:
                    image[k] = 255
                if image[k] < 0:
                    image[k] = 0
                color.append(image[k])
               
            r,g,b = color[0],color[1],color[2]      
            cats.setPixel(i,j,color_rgb(r,g,b))
def specialFilter(cats):
    for i in range(500):
        for j in range(451):
            image = cats.getPixel(i,j)
            r,g,b = image[0],image[1],image[2]
            r = int((r+g+b)/3)
            g = int((r+g+b)/3)
            b = int((r+g+b)/3)
            cats.setPixel(i,j,color_rgb(r,g,b))
def main():
 
    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "white", "Show", Point(150, 40), 45)
    hi = Button(win, "white", "Hide", Point(300, 40), 45)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 150), 45)
    blur = Button(win, "white", "Blur", Point(720, 250), 45)
    cont = Button(win, "white", "Contrast", Point(720, 350), 45)
    filt = Button(win, "white", "Grayscale", Point(720, 450), 45)
 
    cats = Image(Point(400,300), "Cats.png")
 
    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if cont.isClicked(m):
            contrast(cats)
        if filt.isClicked(m):
            specialFilter(cats)
        m = win.getMouse()
 
    win.close()
   
if __name__ == "__main__":
    main()
 


 
