
const main_name = document.querySelector(".window_reload_js");
const click_hiding_logo = document.querySelector("#section_center");

function handleClick_logo(){
    window.location.reload();
    

}

function init(){
    main_name.addEventListener("click", handleClick_logo);
}
init(); 