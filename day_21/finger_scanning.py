import time 
print("""
------------------------------------
          FINGER SCAN            
------------------------------------
"""
)

input("Place the finger and press enter...:")


steps = [
    "Scanning...",
    "Reading Biometrics...",
    "Matching Identity...",
    "Unlocking System..."
]

for s in steps:
    print(s)

    time.sleep(1)

print("Access Granted")
