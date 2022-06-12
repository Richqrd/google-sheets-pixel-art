from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *
import time


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("vick").sheet1

l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']


im = Image.open('photo.jpg') # Can be many different formats.
pix = im.load()

size = list(im.size)
print(size)

for i in range(size[0]):
	for j in range(size[1]):
		data = list(pix[i,j])
		new = [data[0]/255, data[1]/255, data[2]/255]

		fmt = cellFormat(
		    backgroundColor=color(new[0], new[1], new[2]),
		    textFormat=textFormat(bold=True, foregroundColor=color(1, 0, 1)),
		    horizontalAlignment='CENTER'
		    )

		letter = l[i]
		number = j+1
		st = str(letter) + str(number)
		st = st + ':' + st
		print(st)
		format_cell_range(sheet, st, fmt)
		time.sleep(1)








