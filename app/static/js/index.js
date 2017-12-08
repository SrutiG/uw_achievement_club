function showLogin() {
    var loginResources = document.getElementById('login-resources');
    var resourcesText = document.getElementById('resources-text');
    console.log(loginResources.style.display);
    if (loginResources.style.display !== '') {
        loginResources.style.display = '';
        resourcesText.style.display = 'table';
    }
    else {
        loginResources.style.display = 'table';
        resourcesText.style.display = 'none';
    }
};

function addActiveClass() {
    var navbar = document.getElementById("navbar");
    var a = document.getElementsByClassName('nav-item');
    if (window.location.pathname == '/home' || window.location.pathname == '/about' || window.location.pathname == '/resources') {
        navbar.style.backgroundColor = "transparent"
    } else {
        //navbar.style.backgroundColor = "var(--uw_blue)"
        navbar.style.backgroundColor = "transparent"
        for (i = 0; i < a.length; i++) {
            a[i].style.color = "var(--uw_blue)";
        }
    }
    var location = window.location.pathname;
    location = location.replace('/', '')
    elem = document.getElementById(location);
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