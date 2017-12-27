$(document).ready(function() {
    $("#admin-logout").click(function() {
        $.get("/administrator/logout")
          .done(function( data ) {
            window.location.href = '/administrator/login';
        });
    });

    $("#add-location-button").click(function() {
        $.post("/administrator/add_location", {'name':$("#location-name").val(), 'address':$("#location-address").val()})
          .done(function( data ) {
            if (data.success == true) {
                location.reload();
            } else {
                window.alert(data.message);
            }
        }).error(function(error) {
            window.alert(error.message);
        });
    });
});

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

function editLocation(locationName, address) {
    if (locationName === undefined && address === undefined) {
        var oldLocationName = $("#current-location-name").html();
        jQuery.post("/administrator/edit_location", {'name':$("#edit-location-name").val(), 'address':$("#edit-location-address").val(), 'old-name':oldLocationName})
              .done(function( data ) {
                if (data.success == true) {
                    location.reload();
                } else {
                    window.alert(data.message);
                }
            }).error(function(error) {
                window.alert(error.message);
            });
    } else {
        $("#edit-location-modal").modal('show');
        $("#edit-location-name").val(locationName);
        $("#edit-location-address").val(address);
        $("#current-location-name").html(locationName);
    }
}

function deleteLocation(locationName) {
    jQuery.post("/administrator/delete_location", {'name':locationName})
      .done(function( data ) {
        if (data.success == true) {
            location.reload();
        } else {
            window.alert(data.message);
        }
    }).error(function(error) {
        window.alert(error.message);
    });
}