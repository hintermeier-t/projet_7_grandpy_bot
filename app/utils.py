STOP_WORDS = {}
ANSWERS = {}

def log_writer(text):
    with open("templates/log.html", "a") as file
    file.write("<div class=\"messageLine\">",text,"</div>")
    file.close()