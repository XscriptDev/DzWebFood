'use strict';
function Retrieve(){
    console.log('data')
    let s = $(".test2").val()
    console.log(s)
    $.ajax({
        headers: {'X-CSRFToken': '{{ csrf_token }}'},
        method:'POST',
        url:'/ajax',
        data:{
            Codebar:s,
        }, 
        dataType: 'JSON',
        success:function(data){
            console.log(data)
        }
    })
}

$( document ).ready(function() {
    $(function() {
        $("form").submit(function() { return false; });
    });
    $(".test").click(Retrieve);
    $(".test2").keypress(function(e) {e.preventDefault();})
    
    })