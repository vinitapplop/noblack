/**
 * Created by vinit on 05/10/16.
 */
var buildOptGroup = function(d){
    if(d.subCategory != undefined ){
        if(d.subCategory.length == 0){
            var option = $('<option>',{
                text : d['name'],
                value : d['id']
            });
            return option;
        }
        var optGroup = $('<optgroup>', {
            label:d['name'],
            val: d['id']
        });
        for(var i=0;i<d.subCategory.length;i++){
            var temp = buildOptGroup(d.subCategory[i]);
            optGroup.append(temp);
        }
        return optGroup;
    } else {
        var option = $('<option>',{
            text : d['name'],
            value : d['id']
        });
        return option;
    }
    if(d.length == 0){

    } else{

    }

}
$(document).ready(function () {


    $.get('/getStates',function(){
        console.log('State Called');
    })
        .done(function(data){
            var states = data.all_state;
            for(var i=0;i<states.length;i++){
                $('#state').append($('<option>',{
                    value:states[i].id,
                    text: states[i].state_name
                }));
            }
        })
        .fail(function(err){
            console.log(err);
        });
    $('#state').change(function (e) {
        var stateId = $(this).val();
        console.log(stateId);
        $('#city').find("option:gt(0)").remove();
        $.get('/getCities',{'id':stateId},function(){
            console.log('City Called');
        })
            .done(function(data){
                var cities = data.all_city;
                for(var i=0;i<cities.length;i++){
                    $('#city').append($('<option>',{
                        value:cities[i].id,
                        text: cities[i].city_name
                    }));
                }
            })
            .fail(function(err){
                console.log(err);
            })
    });




});