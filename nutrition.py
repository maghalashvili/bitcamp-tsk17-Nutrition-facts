items ={
    "apple": 135,
    "banana": 115,
    "avocado": 160,
    "orange": 50,
    "lime": 45,
}

def main():
    item = input("item:").lower().strip()
    print("Calories:",items[item])
    
main()    