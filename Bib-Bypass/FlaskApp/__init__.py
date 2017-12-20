import scholar
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    print('main...')
    if request.method == 'GET':
        return render_template('index.html')

    keyword_1 = request.form.get('keyword_1')
    keyword_2 = request.form.get('keyword_2')
    keyword_3 = request.form.get('keyword_3')
    keyword_4 = request.form.get('keyword_4')
    citationCount = int(request.form.get('citationCount'))
    keywords = [keyword_1, keyword_2, keyword_3, keyword_4]
    i = 0
    count = 0
    citations = []

    def operation(keyword_x):

        querier = scholar.ScholarQuerier()
        settings = scholar.ScholarSettings()
        querier.apply_settings(settings)

        query = scholar.SearchScholarQuery()
        query.set_author("")
        query.set_words(str(keyword_x))
        query.set_num_page_results(1)

        querier.send_query(query)
        # Print the URL of the first article found
        url = querier.articles[0]['url']
        title = querier.articles[0]['title']
        year = querier.articles[0]['year']
        author = ""
        publication = "Publication"

        line = author + "'" + title + "'. " +
            publication + '. ' + year + ", " + url + "."
        citations.append(line)

    # for keyword in keywords:
    #     if keyword != "":
    #         for i in range(citationCount):
    #             operation(keyword)

    while count < citationCount:
        print('count = ' + str(count))
        print('citationCount = ' + str(citationCount))
        if i == len(keywords):
            i -= len(keywords)

        operation(keywords[i])
        count += 1
        i += 1

    # for i in (keywords):
    #     if count <= citationCount:
    #         if i != "":
    #             count += 1
    #             print(i)
    #             operation(i)

    citations = sorted(citations)
    print(citations)

    return render_template('citation.html', citations=citations)


if __name__ == "__main__":
    app.run()
