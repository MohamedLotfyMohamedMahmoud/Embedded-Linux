"""
1-Make your module that contain favourite websites and have function 
called Firefox take url and open website 
2- then make main file and print menu of sites for user and let him choice
"""

from websites import favourite_websites,open_websit_on_firfox

def print_menu():
    print("Choose a website to open:")
    for key, value in favourite_websites.items():
        print(f"{key}: {value}")

def main():  
    print_menu()
    while True:
        try:
            choice=int(input(f"plz enter your choice (1-{len(favourite_websites)}) :"))
            if 1<=choice<=len(favourite_websites):
                select_site=list(favourite_websites.values())[choice-1]
                open_websit_on_firfox(select_site)
            else:print(f"invalid input .plz enter input from 0 to {len(favourite_websites)}")    
        except ValueError:
            print("Invalid input. pleasse enter a number")

if __name__=="__main__":
    main()

