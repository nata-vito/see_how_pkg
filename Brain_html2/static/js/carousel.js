const carousel = document.getElementById('projects_carousel')
const menu_projects = document.getElementById('popup_menu')
let is_menu = false

carousel.addEventListener(
    "wheel", scroll_carousel, {passive: false}
)

function scroll_carousel(event){
    
    if(!is_menu){
        carousel.scrollBy(event.deltaY*5, 0)
        document.getElementById('projects_sec').scrollIntoView({behavior: 'smooth'})
    }
    else
    {
        menu_projects.scrollBy(event.deltaY*2, 0)
    }
    
}

carousel.onmouseover = function(){
    document.getElementsByTagName('body')[0].style.overflowY = 'hidden';
}

carousel.onmouseleave = function(){
    document.getElementsByTagName('body')[0].style.overflowY = 'scroll';
}

const progress_bar = document.getElementById('progress_bar')

carousel.onscroll = window.onload = function(){
    let progress = carousel.scrollLeft/(carousel.scrollWidth - carousel.clientWidth) * 100
    
    if (progress < 10)
        progress = 10
    
    progress_bar.style.width = progress + '%'
}




menu_projects.addEventListener(
    "wheel", scroll_carousel, {passive: false}
)

menu_projects.onmouseover = function(){
    document.getElementsByTagName('body')[0].style.overflowY = 'hidden';
    is_menu = true
}

menu_projects.onmouseleave = function(){
    document.getElementsByTagName('body')[0].style.overflowY = 'scroll';
    is_menu = false
}