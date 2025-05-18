print("this message will be displayed for everyone")

if __name__ == "__main__":
    print("""this message will be displayed only when the file"
     is executed directly""")
    
    print("""everything under if __name__ == '__main__' will be
     executed only when the file is run directly""")
    

# so when we run this file (directly) it will show:
# this message will be displayed for everyone
# this message will be displayed only when the file" is executed directly
# "everything under if __name__ == '__main__' will be executed
#  only when the file is run directly"


#⁡⁢⁣⁣ but when we import this file to another file it will show:⁡
# this message will be displayed for everyone

