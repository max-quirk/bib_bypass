import scholar
querier = scholar.ScholarQuerier()
settings = scholar.ScholarSettings()
querier.apply_settings(settings)
query = scholar.SearchScholarQuery()

searchphrase = str(input('keyword: '))

def searchScholar(searchphrase):
    query.set_words(searchphrase)
    query.get_url()
    querier.send_query(query)
    print(scholar.csv(querier))

searchScholar('Evaluating technologies for education')