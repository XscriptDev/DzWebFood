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
                let p1='<div class="col"><div class="card padd" style="width: 35rem;" id="' + data.BarCode + '">'
                let img = '<img src=' + data.Image + ' width = "300" height = "300" class="card-img-top" alt="...">'
                let cbody = '<div class="card-body">'
                let form1 = '<form action="/product/add" method="POST">'
                let codebar = '<input type="hidden" id="codebar" name="codebar" value="'+ data.BarCode +'">'
                let pname = '<label class="card-title" for="productname">Product Name:</label><input type="text" id="productname" name="productName" value="'+ data.ProductName +'"><br><br>'
                let brand = '<label class="card-text" for="brand">Brand:</label><input type="text" id="brand" name="brand" value="' + data.Brand + '"><br><br>'
                let ref = '<label class="card-text" for="ref">Reference:</label><input type="text" id="ref" name="ref" value="' + data.ref + '"><br><br>'

                let closing = '<input type="submit" class="btn btn-primary" value="Submit"></form></div></div></div></div>'

                console.log(data)

                $(".jqadd").append(p1 + img + cbody + form1 + codebar + pname + brand+ ref + closing)
                $(".test2").val("");
            },
            error:function (xhr, status, error) {
                alert('CODE BARE Not found!, maybe you misstyped? check again');
                
            }
        })
    });
    $(".test2").keypress(function(e) {
        console.log(Array.from(e.code)[5])
        if(e.key == "Enter") {
            e.preventDefault();
            $(".test").click()                
        }
        
        if (parseInt(Array.from(e.code)[5]) >= 0 && parseInt(Array.from(e.code)[5]) <= 10){
          e.preventDefault();
          let s = $(".test2").val();
          let n = Array.from(e.code)[5];
          $(".test2").val(s + n);
            }
          
    });
})