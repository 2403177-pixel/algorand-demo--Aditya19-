# example.py - simple demo
print("Algorand demo repository - example.py")
try:
    with open("teal/simple.teal", "r") as f:
        print("Contents of teal/simple.teal:")
        print(f.read())
except FileNotFoundError:
    print("teal/simple.teal not found. Make sure the file exists.")
