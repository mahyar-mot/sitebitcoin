$(document).ready(function(){
    (function(){
        p = [];
        var $changePrice = $('.changep');
        var $price = $('.price');
        $changePrice.each(function(i){
            var reg = / -?\d*(\.\d+)?/;
            var res = reg.exec(this.textContent);
            if (parseFloat(res)<0){
                $changePrice[i].classList.add('text-danger');
                $price[i].classList.add('text-danger');
            }else if (parseFloat(res)>0){
                $changePrice[i].classList.add('text-success');
                $price[i].classList.add('text-success');
            }
        });
    })();

});
