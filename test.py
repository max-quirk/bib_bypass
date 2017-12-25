import scholar

querier = scholar.ScholarQuerier()
settings = scholar.ScholarSettings()
querier.apply_settings(settings)

query = scholar.SearchScholarQuery()
query.set_author("Alan Turing")
query.set_words("computing")
query.set_num_page_results(1)

querier.send_query(query)
# Print the URL of the first article found
print querier.articles[0]['url']
