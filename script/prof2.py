import pandas as pd

basedir = r"D:\PythonProj\profile"
staticdir = r"D:\PythonProj\profile\static"
inputdir = r"D:\PythonProj\profile\input"
outputdir = r"D:\PythonProj\profile\output"

experience_dict = {}

to_html = []

df = pd.read_csv(inputdir + "/test.csv", encoding="latin1")
df.fillna("",inplace=True)
for column in df.columns:
    if column == "Summary":
        summary = df["Summary"][0]
        to_html.append("""<h2 id="topic_summary">Summary</h2>""")
        to_html.append("""<p id="content">""" + summary + """</p>""")
    if column == "Experience":
        to_html.append("""<h2 id="topic_experience">Experience</h2>""")
        for i in range(0,len(df["Experience"]), 3):
            #experience_dict[df["Experience"][i]] = [df["Experience"][i+1], df["Experience"][i+2]]
            to_html.append("""<h2 id="companyname">""" + str(df["Experience"][i]) + """</h2>""")
            to_html.append("""<h3 id="companyduration">""" + str(df["Experience"][i+1]) + """</h3>""")
            to_html.append("""<p id="companydetails">""" + str(df["Experience"][i+2]) + """</p>""")
    if column == "Education":
        to_html.append("""<h2 id="topic_education">Education</h2>""")
        for i in range(0,len(df["Education"]), 5):
            #experience_dict[df["Experience"][i]] = [df["Experience"][i+1], df["Experience"][i+2]]
            to_html.append("""<h2 id="course">""" + "<strong>Course: </strong>" + str(df["Education"][i]) + """</h2>""")
            to_html.append("""<h3 id="institute">""" + "<strong>Institute: </strong>" + str(df["Education"][i+1]) + """</h3>""")
            to_html.append("""<p id="board">""" + "<strong>Board: </strong>" + str(df["Education"][i+2]) + """</p>""")
            to_html.append("""<p id="graduation">""" + "<strong>Graduation: </strong>" + str(df["Education"][i+3]) + """</p>""")
            to_html.append("""<p id="percentage">""" + "<strong>Percentage: </strong>" + str(df["Education"][i+4]) + """</p>""")
html_code = """
<!DOCTYPE html>
<html>

<head>
    <!-- <script src="D:\PythonProj\profile\static/prof_scroll.js"></script> -->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/smooth-scroll/16.1.0/smooth-scroll.min.js"></script>
    <script src="{0}/html2pdf.js"></script>
    <link rel="stylesheet" href="{0}/prof.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <div class="navbar">
        <button id="summary" onclick="summary()">Summary</button>
        <button id="experience" onclick="experience()">Experience</button>
        <button id="education" onclick="education()">Education</button>
    </div>
    <div class="main" id="profile_content">
        {1}
    </div>
    <!-- button onclick="generatePDF()">Download as PDF</button> -->
</body>
</html>
""".format(staticdir, "\n".join(to_html))

outfile = open(basedir + "/ashwinberyl.html","w", encoding="latin1")
outfile.write(html_code)
outfile.close()