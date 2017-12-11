var inputNum = 1
var count = 1
console.log('starting...')

function doFirst() {
    var addBtn = document.getElementById('addBtn')
    var keywordsInput = document.querySelectorAll('.keywords')
    var nextBtn = document.getElementById('nextBtn')
    var keywords = document.getElementsByClassName('keywords')
    var input1 = document.getElementById('keyword_1')
    var input2 = document.getElementById('keyword_2')
    var input3 = document.getElementById('keyword_3')
    var input4 = document.getElementById('keyword_4')
    var citeBtn = document.getElementById('citeBtn')
    var numCitations = document.getElementById('numCitations')
    input1.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        addInput(e);
    }
});

input2.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        addInput(e);
    }
});
input3.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        addInput(e);
    }
});
input4.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        addInput(e);
    }
    });
    addBtn.addEventListener('click', addInput, false)
    nextBtn.addEventListener('click', next1, false)
    citeBtn.addEventListener('click', createCitation, false)
}

function addInput() {
    inputNum += 1 
    console.log(inputNum)
    if (inputNum == 2) {
        input2.style.display = 'block'
        window.setTimeout(function ()
    {
        console.log('SET TIMEOUT')
        input2.focus()
    }, 0)
    
}
    if (inputNum == 3) {
        input3.style.display = 'block'
        input3.focus();
    }
    if (inputNum == 4) {
        input4.style.display = 'block'
        input4.focus();
    }
}

function next1() {
    addBtn.style.display = 'none'
    //for(var i=0; i<keywordsInput.length; i++){
    //    keywordsInput[i].style.display = 'none'
    //}
    numCitations.style.display = 'block'
    nextBtn.style.display = 'none'
    citeBtn.style.display = 'block'
}

function createCitation(keywords, citationCount) {
    var keyword_1 = document.getElementById('keyword_1').value
    var keyword_2 = document.getElementById('keyword_2').value
    var keyword_3 = document.getElementById('keyword_3').value
    var keyword_4 = document.getElementById('keyword_4').value
    var citationCount = document.getElementById('citationCount').value
    keywords = [keyword_1,keyword_2,keyword_3,keyword_4]
    // while(count!==numCitations) {
    //     keywords.append(keyword_`${count}`)
    //     count += 1
    // }
    var payload = {keyword:
        keywords,
        citationCount:citationCount
    }

    $(function(){
    $.ajax({
        method: "GET",
        url: "/",
        data: payload
    });
    })
    console.log(keywords)
    console.log(citationCount)
    console.log(payload)
    
}

window.addEventListener("load", doFirst, false)
