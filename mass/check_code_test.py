import validateCodeTool
img,str = validateCodeTool.create_validate_code()
print(str)
with open("check_code.gif","wb") as f:
    img.save(f)