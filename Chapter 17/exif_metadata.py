from exif import Image

with open("BIL.jpg", "rb") as bil:
    photo = Image(bil)
    if photo.has_exif:
        print(photo.get("datetime"))
        print(photo.get("gps_altitude"))
        print(photo.get("gps_longitude"))
        print(photo.get("gps_latitude"))
        print(photo.get("make"))
        print(photo.get("model"))
        print(photo.get("software"))