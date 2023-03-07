const images = document.querySelectorAll("aside .media_content img");
const image = document.getElementById('image_displayed');
const popup_image = document.getElementById('images_display');
let img_bb;

popup_image.addEventListener("mousemove", close_image)

images.forEach(element => {
    element.addEventListener("mouseenter", show_Image);
});

function show_Image(event) {
    if (!popup_image.classList.contains("active"));
        popup_image.classList.add("active");

    image.src = event.target.src;
    img_bb = event.target.getBoundingClientRect();

    image.parentElement.style.animationPlayState = 'running';
}

function close_image(event) {

    //console.log(event)
    if ((event.x < img_bb.left || event.x > img_bb.right) || (event.y < img_bb.top || event.y > img_bb.bottom)) {
        if (popup_image.classList.contains("active"))
            popup_image.classList.remove("active");
    };
}

