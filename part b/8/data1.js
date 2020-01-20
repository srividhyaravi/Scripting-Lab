window.onload=function(){

	models=[
    {
    	"name":"model1",
    	"model":"abc",
    	"price":"4000000",
    	"year":"1999"

    },

     {
    	"name":"model2",
    	"model":"xyz",
    	"price":"6000000",
    	"year":"2001"

    },
     {
    	"name":"model3",
    	"model":"lmn",
    	"price":"5000000",
    	"year":"2000"

    }
    ];

    models.forEach(function(item,index){
      ele=document.createElement("th");
      ele.id=item.model;
      ele.innerHTML=item.name;
      document.getElementById("menu").appendChild(ele);
    })

    models.forEach(mouseEventHandler);
    function mouseEventHandler(item,index){

    	ele=document.getElementById(item.model);
    	ele.onmouseover=function(){


    		document.getElementById("data").removeAttribute("hidden");
    		document.getElementById("name").innerHTML=item.name;
    		document.getElementById("model").innerHTML=item.model;
    		document.getElementById("price").innerHTML=item.price;
    		document.getElementById("year").innerHTML=item.year;
    	}
    }

    }




	
