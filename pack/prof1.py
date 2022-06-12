import pandas as pd

experience_dict = {}

to_html = []

df = pd.read_csv("test.csv", encoding="latin1")

for column in df.columns:
    if column == "Summary":
        summary = df["Summary"][0]
        to_html.append("""<h2 id="topic">Summary</h2>""")
        to_html.append("""<p id="content">""" + summary + """</p>""")
    if column == "Experience":
        to_html.append("""<h2 id="topic">Experience</h2>""")
        for i in range(0,len(df["Experience"]), 3):
            #experience_dict[df["Experience"][i]] = [df["Experience"][i+1], df["Experience"][i+2]]
            to_html.append("""<h2 id="companyname">""" + df["Experience"][i] + """</h2>""")
            to_html.append("""<h3 id="companyduration">""" + df["Experience"][i+1] + """</h3>""")
            to_html.append("""<p id="companydetails">""" + df["Experience"][i+2] + """</p>""")
html_code = """
<!DOCTYPE html>
<html>

<head>
    <script src="prof.js"></script>
    <link rel="stylesheet" href="prof.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <div class="navbar">
        <button>Summary</button>
        <button onclick="experience()">Experience</button>
        <button>Skills</button>
    </div>

    <div class="main">
        {}
    </div>
</body>
</html>
""".format("\n".join(to_html))

outfile = open("profile_001.html","w", encoding="latin1")
outfile.write(html_code)
outfile.close()