import scholar
import random
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('title.html')

    keyword_1 = request.form.get('keyword_1')
    keyword_2 = request.form.get('keyword_2')
    keyword_3 = request.form.get('keyword_3')
    keyword_4 = request.form.get('keyword_4')
    citationCount = int(request.form.get('citationCount'))

    keywords = [keyword_1, keyword_2, keyword_3, keyword_4]

    keywords = [i for i in keywords if len(i.strip()) > 0]

    print(keywords)
    i = 0
    x = 0
    count = 0
    citations = []

    first_names = ["A", "B", "C", "D", "E", "F", "G",
                   "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "V", "W", "Z"]

    with open("last_names.txt", "r") as data:
        last_names = data.readlines()

    def operation(keyword_x, index):
        print('index: ' + str(index))
        print('keyword: ' + str(keyword_x))
        index = int(index)

        querier = scholar.ScholarQuerier()
        settings = scholar.ScholarSettings()
        querier.apply_settings(settings)

        query = scholar.SearchScholarQuery()
        query.set_author("")
        query.set_words(str(keyword_x))
        query.set_num_page_results(10)

        querier.send_query(query)

        try:
            url = querier.articles[index]['url'].encode('utf-8')
        except AttributeError:
            url = "No URL"

        try:
            title = querier.articles[index]['title'].encode('utf-8')
        except AttributeError:
            url = "No Title"

        try:
            year = querier.articles[index]['year'].encode('utf-8')
        except AttributeError:
            year = "No Date"

        author = random.choice(last_names).strip() + \
            ", " + random.choice(first_names) + ". " + " '"

        line = author + title.decode('utf-8') + \
            "'. " + \
            year.decode('utf-8') + ", " + url.decode('utf-8') + "."

        print(line)

        citations.append(line)

    while count < citationCount:
        if i == len(keywords):
            i -= len(keywords)
            x += 1

        while True:
            try:
                operation(keywords[i], x)
                break
            except IndexError:
                if not keywords:
                    break

                else:
                    keywords.remove(keywords[i])
                    if i == len(keywords):
                        i -= len(keywords)
                        x += 1

        count += 1
        i += 1

    citations = sorted(citations)

    if len(citations) != citationCount:
        if not citations:
            citations.append('Sorry, no results.')
        else:
            citations.append('Sorry, could not find %s results.' %
                             citationCount)

    return render_template('citation.html', citations=citations)


if __name__ == "__main__":
    app.run()
