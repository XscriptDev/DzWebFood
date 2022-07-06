'use strict';
$( document ).ready(function() {
    $(".test").click(function(){
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
    });
})