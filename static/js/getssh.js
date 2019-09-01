	$(function(){


		$("#submitSSH").on("click",function(){
			//alert("into");
			var data=$("#command").val();
			//alert(data);
		$.ajax({
        type:'get',
        url:'/get_ssh',
        data:{name:data},
		async:true,
        dataType:'json',//希望服务器返回json格式的数据
        success:function(data){
        	//alert("into");
        	//alert(data.stdout);
        	//alert($("#ssh").html());
        	//var temp_p = document.createElement("p");
        	//temp_p.innerText="this is ";
        	//$("#sshcontent").append(temp_p);
        	$("#ssh").text(data.stdout);
        	//alert("out");
		}
		});
		});
    });