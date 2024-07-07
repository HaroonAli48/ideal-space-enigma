const display=document.getElementById("display");
const keys=document.getElementById("keys");
var i=0;
function appendToDisplay(input){
    display.value += input;
}
function clearDisplay(){
    display.value="";

}
function calculate(){
     try{
        display.value = eval(display.value);
     }
    catch(error){
        display.value="Error";
    }
}
if(display.value === "Error"){
keys.addEventListener("click", function(event) {
    const key = event.target;
    const keyValue = key.textContent;

    if (display.value === "Error") {
        clearDisplay();
    }

    if (keyValue === "=") {
        calculate();
    } else if (keyValue === "C") {
        clearDisplay();
    } else {
        appendToDisplay(keyValue);
    }
});
}