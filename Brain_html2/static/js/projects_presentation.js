const popup = document.getElementById("projects_popup");
const projects = document.querySelectorAll("#projects_popup .project");
const menu = document.querySelectorAll(".menu_item")
let current = 0;
let previous = 0;

function openProject(project) {

    //"If" in specific cases to use next and previous buttons
    if (project == -2)
        current += 1   // next project
    else if (project == -1)
        current -= 1;  // previous project
    else
        current = project;
    
    
    //"If" for the case of list ends 
    if (current > projects.length-1)
        current = projects.length-1;
    else if (current < 0)
        current = 0;
    
    // Active popup
    if (!popup.classList.contains("active"))
        popup.classList.add("active");
    
    
    if (current != previous){
        projects[current].classList.add("active");
        projects[previous].classList.remove("active");
        menu[current].classList.add("active");
        menu[previous].classList.remove("active");
    }

    previous = current;
}

document.addEventListener("keyup", function(event) {

    if (popup.classList.contains("active"))
    {
        if (event.key == 'Escape')
            popup.classList.remove("active");
        else if (event.key == 'ArrowRight')
            openProject(-2);
        else if (event.key == 'ArrowLeft')
            openProject(-1);
    }
    
 });