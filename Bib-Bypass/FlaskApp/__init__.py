from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def hello():
    print('main...')
    return render_template('index.html')

    if request.method == 'GET':
        print('changing...')

    payload = request.form('payload')
    keywords = payload(keywords)
    citationCount = payload(citationCount)
    citations = []
    count = 0

    def operation(keyword):
        count += 1
        line = keyword
        citations.append(line)
    
    while count <= citationCount:
        for i in keywords:
            operation(i)

    citations = sorted(citations)

    print(citations)

@app.route("/citation", methods=["GET", "POST"])
def citation():
    print("citation...")
    return render_template('citation.html', cite1=citations[0],  cite2=citations[1], 
        cite3=citations[2], cite4=citations[3],  cite5=citations[4],  cite6=citations[5], 
        cite7=citations[6], cite8=citations[7],  cite9=citations[8], cite10=citations[9],  
        cite11=citations[10], cite12=citations[11],  cite13=citations[12],  cite14=citations[13],  
        cite15=citations[14], cite16=citations[15],  cite17=citations[16],  cite18=citations[17])

if __name__ == "__main__":
    app.run()

