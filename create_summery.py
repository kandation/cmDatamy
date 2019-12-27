import os
import webbrowser

f = open("t.html","w+")
text = "<html>\n<heah>\n\t<title>none</title>\n<head>\n"
end = "<body>ffffdss</body>\n</html>"

text += """
<table border = 1>
<tr><th>aaaaa</th><th>ssssss</th></tr>
<tr><td>sss</td><td>dd</td></tr>
<tr><td>0</td><td>1</td></tr>
"""
for pp in range(5):
    text += "<tr><td>ddddddd</td><td>ddddddd</td></tr>"
"""
<tr><td>0</td><td>1</td></tr>
</table>
"""

f.write(text+end)
webbrowser.open_new_tab(os.getcwd()+"\\t.html")
