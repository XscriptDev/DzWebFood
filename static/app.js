'use strict';

$( document ).ready(function() {
    $(function() {
        $("form").submit(function() { return false; });
    });
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

                $(".jqadd").append('<div class="col"><div class="card padd" style="width: 35rem;"><img src="'+data.Image +'" class="card-img-top" width = "300" height = "300" alt="..."><div class="card-body"><h5 class="card-title">'+data.ProductName+'</h5><input class="card-text">Marque:'+data.Brand  +'</p><a href="#" class="btn btn-primary">SAVE</a></div>')
            },
            error:function (xhr, status, error) {
                alert('CODE BARE Not found!, maybe you misstyped? check again');
            }
        })
    });
    $(".test2").keypress(function(e) {
        console.log(e.code)
        if(e.key == "Enter") {
            e.preventDefault();
            $(".test").click()                
        }
        
        if (parseInt(e.code) >= 48 && parseInt(e.code) <= 57){
          e.preventDefault();
          let s = $(".test2").val();
          let n = parseInt(e.code) - 48;
          $(".test2").val(s + n);
            }
          
    });
})