from flask import Flask, render_template, request

app = Flask(__name__)

# Skills Database
job_skills = {
    "Python Developer": [
        "python", "flask", "django", "sql",
        "html", "css", "javascript"
    ],

    "Web Developer": [
        "html", "css", "javascript",
        "bootstrap", "php", "mysql"
    ],

    "Java Developer": [
        "java", "jdbc", "jsp",
        "servlet", "mysql", "html"
    ],

    "Data Analyst": [
        "python", "excel", "sql",
        "power bi", "tableau"
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        name = request.form["name"]
        role = request.form["role"]
        resume = request.form["resume"].lower()

        required = job_skills.get(role, [])

        found = []
        missing = []

        for skill in required:
            if skill in resume:
                found.append(skill)
            else:
                missing.append(skill)

        if len(required) > 0:
            percentage = int((len(found) / len(required)) * 100)
        else:
            percentage = 0

        if percentage >= 80:
            status = "Excellent Match"
        elif percentage >= 60:
            status = "Good Match"
        elif percentage >= 40:
            status = "Average Match"
        else:
            status = "Need More Skills"

        result = {
            "name": name,
            "role": role,
            "percentage": percentage,
            "found": found,
            "missing": missing,
            "status": status
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)