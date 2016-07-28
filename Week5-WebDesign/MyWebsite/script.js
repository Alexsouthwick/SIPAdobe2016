$(document).ready(function() {
    // $("#pinterest_tour").hide();
    // $("#pinterest_lunch").hide();
    $("button").on("click", plusDivs(+1));
    $("button").on("click", plusDivs(-1));
});



        var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("photos");
    if (n > x.length) {slideIndex = 1} 
    if (n < 1) {slideIndex = x.length} ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none"; 
    }
    x[slideIndex-1].style.display = "block"; 
}


// var original_picture= '#pinterest_tour'
//     var new_picture = '#pinterest_sign'
//         var new_src= $(original_picture).attr('src');
//         $(new_picture).attr('src', new_src);
//      original_picture='#pinterest_sign'
//      new_picture= '#pinterest_lunch'

//         $(new_picture).attr('src', new_src);


