var operator; 
function func() {
    var result;
    var number1 = Number(document.getElementById("number1").value);
    var number2 = Number(document.getElementById("number2").value);
    switch (operator) {
        case '+':
            result = number1 + number2;
            break;
        case '-':
            result = number1 - number2;
            break;
        case '*':
            result = number1 * number2;
            break;
        case '/':
            result = number1 / number2;
            break;
    }
}
alert("USATU{tHiS_c0dE_do3snT_MaK3_sENse}");