#task- 4  function to detect measurement scale 

def detect_scale(data):
    if all(isinstance(x,str)for x in data):
        if all(x in ["pending","shipped","delivered"] for x in data):
            return "ordinal scale"
        else:
            return "nominal scale"

    elif all(isinstance(x,(int,float))for x in data):
        if all(x >=0 for x in data):
            if 0 in data:
               return "ratio scale"
            elif all(x==int(x) for x in data):
              return "intervel scale"
        else:
          return "check intervel or ratio scale"
    else:
       return "mixed data - manually scale"

print(detect_scale (["UPI","cash","card"]))
print(detect_scale(["pending","shipped","delivered"]))
print(detect_scale([0,100,200,500]))
print(detect_scale([10,20,30,40]))        