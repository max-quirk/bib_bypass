import scholar
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    print('main...')
    if request.method == 'GET':
        return render_template('title.html')

    keyword_1 = request.form.get('keyword_1')
    keyword_2 = request.form.get('keyword_2')
    keyword_3 = request.form.get('keyword_3')
    keyword_4 = request.form.get('keyword_4')
    citationCount = int(request.form.get('citationCount'))
    print('citationCount = ' + str(citationCount))
    keywords = [keyword_1, keyword_2, keyword_3, keyword_4]
    print('original keywords = ' + str(keywords))
    print('keyword_4 = ' + str(keyword_4))
    print('keyword[3] = ' + str(keywords[3]))

    keywords = [i for i in keywords if len(i.strip()) > 0]

    print(keywords)
    i = 0
    count = 0
    citations = []

    def operation(keyword_x, index):
        print('index: ' + str(index))
        index = int(index)

        querier = scholar.ScholarQuerier()
        settings = scholar.ScholarSettings()
        querier.apply_settings(settings)

        query = scholar.SearchScholarQuery()
        query.set_author("")
        query.set_words(str(keyword_x))
        query.set_num_page_results(5)

        querier.send_query(query)
        # Print the URL of the first article found
        url = str(querier.articles[index]['url'])
        title = str(querier.articles[index]['title'])
        year = str(querier.articles[index]['year'])
        author = ""
        publication = "Publication"

        line = author + "'" + title + "'. " + \
            publication + ". " + year + ", " + url + "."

        print(line)

        citations.append(line)

    # for keyword in keywords:
    #     if keyword != "":
    #         for i in range(citationCount):
    #             operation(keyword)

    while count < citationCount:
        print('count = ' + str(count))
        print('len(keywords) = ' + str(len(keywords)))
        if i == len(keywords):
            i -= len(keywords)

        if count < len(keywords):
            operation(keywords[i], 0)

        elif count >= len(keywords) and count < (2 * len(keywords)):
            operation(keywords[i], 1)

        elif count >= (2 * len(keywords)) and count < (3 * len(keywords)):
            operation(keywords[i], 2)

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
