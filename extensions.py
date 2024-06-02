fname = input("File name: ").strip().lower()

if fname.endswith(".jpg") or fname.endswith("jpeg"):
    print("image/jpeg")
elif fname.endswith(".png"):
    print("image/png")
elif fname.endswith(".zip"):
    print("application/zip")
elif fname.endswith(".txt"):
    print("text/plain")
elif fname.endswith(".gif"):
    print("image/gif")
elif fname.endswith(".pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")








