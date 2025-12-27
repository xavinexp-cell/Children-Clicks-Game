import intrographics

def left_click(x,y):
    box = window.rectangle(x-10, y-10, 20,20)
    box.fill("blue")
    box.group("boxes")
    
def right_click(x,y): 
    for box in window.all("boxes"): 
        if box.occupies(x,y):       
            window.remove(box)        

window = intrographics.window(400,400)
window.on_left_click(left_click)
window.on_right_click(right_click)


window.open()