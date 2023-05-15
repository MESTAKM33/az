const bar = document.getElementById ('bar');
const close = document.getElementById('close')
const nav = document.getElementById('navbar');
    bar.onclick = function() {
     nav.classList.toggle('active')
}
if (close){
    close.addEventListener ('click', () =>{
        nav.classList.remove('active');
    })
}
if(document.readyState == "loading"){
    document.addEventListener('DOMContentLoaded', start);
}else{
    start();
}
function start (){
    addEvents();
}
function update(){
    addEvents();
}
function addEvents(){
    let cartRemove_btns = document.querySelectorAll('.close-cart');
    console.log(cartRemove_btns);
    cartRemove_btns.forEach((btn) => {
        btn.addEventListener("click", handle_removeCartItem);
    });
}
function handle_removeCartItem() {
    this.parentElement.remove();
}
