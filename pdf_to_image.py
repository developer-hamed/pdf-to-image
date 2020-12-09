#python script to take screenshot from pdf pages
#this could be handy when the pdf print option is password protected
#or you can use it to take screenshot from DRM protected ebooks and
#then use OCR to make a new pdf without DRM!
import pyautogui, time, pyscreenshot, os

def take_screeshot_from_page(page_number, x1, y1, x2, y2):
    time.sleep(1)
    #enters page number in page number box to change page
    pyautogui.typewrite(str(page_number))
    pyautogui.press("enter")
    #takes and saves screenshot from (x1, y1) to (x2, y2) area
    image = pyscreenshot.grab(bbox=(x1, y1, x2, y2)) 
    image.save("Images//" + str(page_number) + ".png")

def main():
    #makes a directory named "Images"
    if(not os.path.exists(os.path.abspath(os.getcwd()) + "\\Images")):
        os.makedirs(os.path.abspath(os.getcwd()) + "\\Images")   
    
    #you can use mouse position finder to find (x1, y2) and (y1, y2)
    x1 = int(input("Enter x1 : "))
    y1 = int(input("Enter y1 : "))
    x2 = int(input("Enter x2 : "))
    y2 = int(input("Enter y2 : "))
    start = int(input("Enter start page : "))
    end = int(input("Enter end page : "))
    
    input("Make the screen ready, press enter and click on page number text box")
    print("Starting in 10 seconds")
    time.sleep(10)

    for i in range(start, end + 1):
        take_screeshot_from_page(i, x1, y1, x2, y2)
    
    input("Done!")

if __name__ == "__main__":
    main()