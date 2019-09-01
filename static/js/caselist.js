	$(function(){

		$.ajax({
        type:'get',
        url:'/show_case',
		async:true,
        dataType:'json',//希望服务器返回json格式的数据
        success:function(data){
        	//alert(data.showcase.length);
        	if(data.statue=="1") {
				for (var j = 0; j < data.showcase.length; j++) {
					var temp_tr = document.createElement("tr");
					var temp_td1 = document.createElement("td");
					var temp_td2 = document.createElement("td");
					var temp_td3 = document.createElement("td");
					var temp_td4 = document.createElement("td");
					var temp_td5 = document.createElement("td");
					var temp_td6 = document.createElement("td");
					var temp_td7 = document.createElement("td");
					var temp_td8 = document.createElement("td");
					var temp_inp = document.createElement("input");
					var temp_div = document.createElement("div");
					var temp_a1 = document.createElement("a");
					var temp_a2 = document.createElement("a");
					//var temp_a3 = document.createElement("a");
					var temp_but1 = document.createElement("button");
					var temp_but2 = document.createElement("button");
					var temp_but3 = document.createElement("button");

					temp_inp.type = "checkbox";
					temp_td2.innerText = data.showcase[j][0];
					temp_td3.innerText = data.showcase[j][1];
					temp_td4.innerText = data.showcase[j][2];
					temp_td5.innerText = data.showcase[j][3];
					temp_td6.innerText = data.showcase[j][4];
					temp_td7.innerText = data.showcase[j][5];
					temp_div.className = "tools";
					//temp_a1.href = "/file-manage";
					temp_but1.type = "button";
					temp_but1.className = "btn btn-default";
					temp_but1.innerText = "文件管理";
					temp_a1.href = "/file-manage";
					temp_but2.type = "button";
					temp_but2.className = "btn btn-default";
					temp_but2.innerText = "编辑";
					temp_a2.href = "/editshili";
					//temp_a3.href = "/add_register?name=" + data.userregister1[j][1];
					temp_but3.type = "button";
					temp_but3.className = "btn btn-default";
					temp_but3.innerText = "删除";
					temp_but3.onclick=function f() {
	 if(confirm('确定删除该实例?'))
    {
        window.location.href='/delcase';
    	return true;
    }
    return false;
};



					//alert(data.userregister1[0]);
					temp_td1.appendChild(temp_inp);
					temp_a1.appendChild(temp_but1);
					//temp_a2.appendChild(temp_but1);
					temp_a2.appendChild(temp_but2);
					//temp_a3.appendChild(temp_but3);
					temp_div.appendChild(temp_a1);
					temp_div.appendChild(temp_a2);
					temp_div.appendChild(temp_but3);
					temp_td8.appendChild(temp_div);
					temp_tr.appendChild(temp_td1);
					temp_tr.appendChild(temp_td2);
					temp_tr.appendChild(temp_td3);
					temp_tr.appendChild(temp_td4);
					temp_tr.appendChild(temp_td5);
					temp_tr.appendChild(temp_td6);
					temp_tr.appendChild(temp_td7);
					temp_tr.appendChild(temp_td8);
					//alert("into end");
					$("#caseshow").find("tbody").append(temp_tr);
				}
			}
		}
		});




    });

