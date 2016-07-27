$(document).ready(function() {
    $("#pinterest_tour").hide();
    $("#pinterest_lunch").hide();
    $('#next').on("click", change_picture);
});


function change_picture(){
    var original_picture= '#pinterest_tour'
    var new_picture = '#pinterest_sign'
        var new_src= $(original_picture).attr('src');
        $(new_picture).attr('src', new_src);
     original_picture='#pinterest_sign'
     new_picture= '#pinterest_lunch'

        $(new_picture).attr('src', new_src);
    }



    // var source= $('#pinterest_sign.src');
    // console.log(source);
    // source= $('#pinterest_tour.src');
    // console.log(source);

