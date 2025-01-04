from PIL import Image  
import pytesseract 
img=Image.open('expression.png')
text=pytesseract.image_to_string(img)
print("Extracted Text:",text.strip())
try:
    result=eval(text.strip())
    print("Result:",result)
except Exception as e:
    print("Couldn't evaluate the expression!", e)
