var numberRandom;
var attemptNumber = 0
$(document).ready(function () {
    numberRandom = Math.round(Math.random() * 100);
   

    $(".tryTxt").click(function(){
        $('.tryBtn').popover("destroy");
    })

})
function attempt(){
    var guess = $('.tryTxt').val();
    var status
    if(guess/1 && guess>=0 && guess<=100){
        if(guess < numberRandom){
            status = "<td class='warning'>bellow</td>";

        }else if(guess > numberRandom){
            status = "<td class='info'>above</td>";
        }else{
            status = "<td class='success'>Right</td>";
            $('.tryBtn').html("Play again");
            $('.tryBtn').attr("onclick", "playAgain()");
            $('.tryBtn').removeClass("btn-primary").addClass("btn-success");
        }
        $('tbody:last-child').append("<tr><td>"+ ++attemptNumber +"</td><td>"+ guess +"</td>"+ status +"</tr>")
    }else{
        $('.tryBtn').popover({
            title: "<p style = 'color:red;'>Error</p>",
            content: 'This value is not acceptable',
            placement: 'right',
            html: 'true'
        })
        $('.tryBtn').popover('show');
    }

}

function playAgain(){
    location.reload(true);
}