function addActiveClass() {
    var navbar = document.getElementById("navbar");
    if (window.location.pathname == '/home') {
        navbar.style.backgroundColor = "transparent"
    } else {
        navbar.style.backgroundColor = "var(--uw_blue)"
    }
    var location = window.location.pathname;
    location = location.replace('/', '')
    elem = document.getElementById(location);
    var a = document.getElementsByClassName('nav-item');
    for (i = 0; i < a.length; i++) {
        a[i].classList.remove('active');
    }
    elem.classList.add('active');
}

function showDescript(elem) {
    var goal = elem.id;
    var goalDescript = document.getElementById(elem.id + '_desc');
    if (goalDescript.style.display === "") {
        goalDescript.style.display = "table";
    }
}

function hideDescript(elem) {
    var goal = elem.id;
    var goalDescript = document.getElementById(elem.id + '_desc');
    if (goalDescript.style.display === "table") {
        goalDescript.style.display = "";
    }
}