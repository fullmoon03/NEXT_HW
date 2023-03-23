from bs4 import BeautifulSoup
import requests as req
import pandas as pd

url_target = "https://opentutorials.org/course/1"
res = req.get(url_target)
soup = BeautifulSoup(res.text, "html.parser")

li_comment = soup.select('div.comment_content')
li_comment_processed = [e.text.strip() for e in li_comment]

li_name = soup.select('div.name.time > strong') 
li_name_processed = [e.text for e in li_name]

li_time = soup.select('div.name.time > a > time')
li_time_processed = [e.text for e in li_time]
context = {'name': li_name_processed, 'time': li_time_processed, 'comments': li_comment_processed}
df_table = pd.DataFrame(context)
df_table