import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://vimeo.com/260088074")
arctic_monkeys_url = urlopen("https://media.giphy.com/media/rgzOwma0qMbM3x7Fqi/giphy.gif")
slts_qrcode.to_artistic(
    background=arctic_monkeys_url,
    target="animated_qrcode.gif",
    scale=5,
)


#https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnk0a2tnd200NWYyODlkY3dwZ2NxM3VtMTU5aXZ4dmdhYnZ6NTljYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/b8RfbQFaOs1rO10ren/giphy.gif #the office gif
#https://media.giphy.com/media/rgzOwma0qMbM3x7Fqi/giphy-downsized-large.gif # tech gif
#https://media.giphy.com/media/rgzOwma0qMbM3x7Fqi/giphy.gif


make a python script that ask the User for Client ID, Project ID as well as the Room ID. It then
will generate a qr code that will store the three values as a json object. 