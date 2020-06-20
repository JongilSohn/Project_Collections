const pocket_bar_1 = document.querySelector("#fixedbtn")
const tooltip = document.querySelector(".balloon")

const balloon = "balloon hiding_class"



function handleClick_tooltip() {
    const current_class = tooltip;

    if(current_class.className == balloon){
        tooltip.classList.remove('hiding_class');
    }
    else{
        tooltip.classList.add('hiding_class');
    }

}


function init() {
    pocket_bar_1.addEventListener("click", handleClick_tooltip);
}
init()