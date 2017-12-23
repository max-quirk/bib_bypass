var inputNum = 1
var count = 1
console.log('correct version')

function doFirst() {
    var addBtn = document.getElementById('addBtn')
    var keywordsInput = document.querySelectorAll('.keywords')
    var keywords = document.getElementsByClassName('keywords')
    var input1 = document.getElementById('keyword_1')
    var input2 = document.getElementById('keyword_2')
    var input3 = document.getElementById('keyword_3')
    var input4 = document.getElementById('keyword_4')
    var citeBtn = document.getElementById('citeBtn')
    var numCitations = document.getElementById('numCitations')
    var surely = document.getElementById('surely')
    var form_div = document.getElementById('form_div')
    var step2 = document.getElementById('step2')
    var bottom = document.getElementById('bottom')
    var title_button = document.getElementById('title_button')
    var firstPage = document.getElementById('firstPage')

    title_button.addEventListener("click", change, false)
    citeBtn.addEventListener("click", clickedCite)

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
}

function change() {
    firstPage.style.display = 'none'
    form_div.style.display = 'block'
    console.log('title_page')
}

function addInput() {
    inputNum += 1
    console.log(inputNum)
    if (inputNum == 2) {
        input2.style.display = 'block'
        window.setTimeout(function () {
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
        addBtn.style.display = 'none'
        input4.focus();
    }
}

function next1() {
    console.log(123)
    addBtn.style.display = 'none'
    //for(var i=0; i<keywordsInput.length; i++){
    //    keywordsInput[i].style.display = 'none'
    //}
    nextBtn.style.display = 'none'
    step2.style.display = 'block'
    bottom.style.display = 'block'

}

function clickedCite() {
    console.log('clicked site')
    surely.style.display = 'block'
    main.style.display = 'none'
}


window.addEventListener("load", doFirst, false)
