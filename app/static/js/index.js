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

    $("#crop-success-button").click(function() {
        var cropped = $("#show-success-img").cropper('getCroppedCanvas').toDataURL('image/png');
        $("#cropped-success-img").attr('src', cropped);
        $("#upload-success-img").show();
    });

    $("#uploadimg").click(function() {
        $("#show-success-img").cropper('getCroppedCanvas').toBlob(function (blob) {
            var formData = new FormData();
            var fileName = $("#success-photo").val();
            formData.append('croppedImage', blob);
            formData.append('filename', fileName);
            $.ajax('/getImage', {
                method: "POST",
                data: formData,
                processData: false,
                contentType: false,
                success: function () {
                  console.log('Upload success');
                  $("#success-story-form").submit();
                },
                error: function () {
                  window.alert('Error uploading image');
                }
            });
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

function readURL(input) {
    $("#show-success-img").cropper('destroy');
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
        $('#show-success-img').attr('src', e.target.result);
        $('#show-success-img').cropper({
          aspectRatio: 10 / 10,
          scalable: false,
          zoomOnTouch: false,
          zoomable:false
        });
    }
        reader.readAsDataURL(input.files[0]);
        $("#crop-success-button").show();
    }
}

function openSuccessModal() {
    $("#success-photo").val(null);
    $("#show-success-img").cropper('destroy');
    $("#show-success-img").attr('src', "#");
    $("#crop-success-button").hide();
    $("#cropped-success-img").attr('src', '/static/images/success_story/default_user_img.png');
}

