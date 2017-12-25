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
        print('keyword: ' + str(keyword_x))
        index = int(index)

        querier = scholar.ScholarQuerier()
        settings = scholar.ScholarSettings()
        querier.apply_settings(settings)

        query = scholar.SearchScholarQuery()
        query.set_author("")
        query.set_words(str(keyword_x))
        query.set_num_page_results(11)

        querier.send_query(query)
        # Print the URL of the first article found
        url = querier.articles[index]['url'].encode('utf-8')
        title = querier.articles[index]['title'].encode('utf-8')
        year = querier.articles[index]['year'].encode('utf-8')

        author = ""
        publication = ""

        line = """author.decode('utf-8') +""" "'" + title.decode('utf-8') + \
            "'. " """+ publication.decode('utf-8') + ". " """ + \
            year.decode('utf-8') + ", " + url.decode('utf-8') + "."

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
            x = 0
        # WILL FIX THIS UP:
        elif count >= len(keywords) and count < (2 * len(keywords)):
            x = 1

        elif count >= (2 * len(keywords)) and count < (3 * len(keywords)):
            x = 2

        elif count >= (3 * len(keywords)) and count < (4 * len(keywords)):
            x = 3

        elif count >= (4 * len(keywords)) and count < (5 * len(keywords)):
            x = 4

        elif count >= (5 * len(keywords)) and count < (6 * len(keywords)):
            x = 5

        elif count >= (6 * len(keywords)) and count < (7 * len(keywords)):
            x = 6

        elif count >= (7 * len(keywords)) and count < (8 * len(keywords)):
            x = 7

        elif count >= (8 * len(keywords)) and count < (9 * len(keywords)):
            x = 8

        elif count >= (9 * len(keywords)) and count < (10 * len(keywords)):
            x = 9
        try:
            operation(keywords[i], x)
        except IndexError:
            keywords.remove(keywords[i])
            x += 1
            if not keywords:
                break
            operation(keywords[i], x)

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

    if len(citations) != citationCount:
        if not citations:
            citations.append('Sorry, no results')
        else:
            citations.append('Sorry, could not find %s results' %
                             citationCount)

    return render_template('citation.html', citations=citations)


if __name__ == "__main__":
    app.run()
