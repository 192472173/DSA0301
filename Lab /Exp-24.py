dialog = input("Enter sentence: ")

if dialog.endswith("?"):
    print("Dialog Act: Question")

elif dialog.lower().startswith("please"):
    print("Dialog Act: Request")

else:
    print("Dialog Act: Statement")
