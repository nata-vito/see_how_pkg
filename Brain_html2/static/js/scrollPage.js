const body = document.getElementsByTagName('body')[0]
let scrollerID;
let paused = true;
let speed = 5; // 1 - Fast | 2 - Medium | 3 - Slow
let interval = speed * 5;

function startScroll(){
    console.log('started');
    let id = setInterval(function() {
        window.scrollBy(0, 2);
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            // Reached end of page
            stopScroll();
        }
    }, interval);
    return id;
}

function stopScroll() {
    clearInterval(scrollerID);
}

function scrolling() {
    
    if(paused == true) {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight)
            window.scrollTo(0, 500, { behavior: 'smooth' })
        scrollerID = startScroll();
        paused = false;
    }
    else {
        stopScroll();
        paused = true;
    }
}

document.body.addEventListener('keypress', function (event)
{
    if (event.key == 'p') {
        // It's the 'P' key
        scrolling();
    }
}, true);
