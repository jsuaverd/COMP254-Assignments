

color1 =["red", "green", "green"]
pattern = ["a", "b", "b"]
color2 =["red", "green", "greenn"]

def samePatterns(color,pattern):
    if color+pattern==["red", "green", "green","a", "b", "b"]:
        return True
    else:
        return False
    
print(samePatterns(color1,pattern))
print(samePatterns(color2,pattern))

