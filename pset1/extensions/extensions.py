x = input("File name: ").strip().lower().split(".")
x = x[-1]

if x == "gif":
    print("image/gif")
elif x == "jpg" or x == "jpeg":
    print("image/jpeg")
elif x == "png":
    print("image/png")
elif x == "pdf":
    print("application/pdf")
elif x == "txt":
    print("text/plain")
elif x == "zip":
    print("application/zip")
else:
    print("application/octet-stream")