	$(function(){
		var  data="";
		$.ajax({
        type:'GET',
        url:'/get_file',
        data:{name:data},
		async:true,
        dataType:'json',//希望服务器返回json格式的数据
        success:function(data){
						var flen = data.filename.length;
						var dlen = data.dirname.length;
						$('#fileTree').find("tbody").empty();
						for (var i = 0; i < flen; i++) {
							var temp_tr = document.createElement("tr");
							var temp_td1 = document.createElement("td");
							var temp_td2 = document.createElement("td");
							var temp_td3 = document.createElement("td");
							var temp_td4 = document.createElement("td");

							//var temp_a = document.createElement("a");

							temp_td1.innerText = "文件";
							temp_td2.innerText = data.filename[i];
							if (data.resultfile[i]=="1"){
								temp_td4.innerText = "拥有权限";
							} else if(data.resultfile[i]=="0"){
								temp_td4.innerText = "无权限访问";
							}
							//alert("into this");
							temp_tr.appendChild(temp_td1);
							temp_tr.appendChild(temp_td2);
							temp_tr.appendChild(temp_td3);
							temp_tr.appendChild(temp_td4);
							$("#fileTree").find("tbody").append(temp_tr);
						}
						for (var i = 0; i < dlen; i++) {
							//alert("into dir");
							var atemp_tr = document.createElement("tr");
							var atemp_td1 = document.createElement("td");
							var atemp_td2 = document.createElement("td");
							var atemp_td3 = document.createElement("td");
							var atemp_td4 = document.createElement("td");
							//var temp_a = document.createElement("a");

							atemp_td1.innerText = "文件夹";
							atemp_td2.innerText = data.dirname[i];
							if (data.resultdir[i]=="1"){
								atemp_td4.innerText = "拥有权限";
							} else if(data.resultdir[i]=="0"){
								atemp_td4.innerText = "无权限访问";
							}
							atemp_tr.appendChild(atemp_td1);
							atemp_tr.appendChild(atemp_td2);
							atemp_tr.appendChild(atemp_td3);
							atemp_tr.appendChild(atemp_td4);
							$("#fileTree").find("tbody").append(atemp_tr);
						}
        }
    });

		$("#fileTree tbody").on("click","tr",function() {
			//alert("into this tr");
			var td = $(this).find("td");
			var mid = td.eq(0).text();
			var auth = td.eq(3).text();
			//alert(auth);
			if (auth=="拥有权限") {
				if (mid=="文件夹") {
				data=td.eq(1).text();
				//alert(data);
				//alert("data");
				$.ajax({
					type: 'GET',
					url: '/get_file',
					data: {name: data},
					async: true,
					dataType: 'json',//希望服务器返回json格式的数据
					success: function (data) {
						//alert(data.filename.length);
						//alert(data.dirname.length);
						var flen = data.filename.length;
						var dlen = data.dirname.length;
						$('#fileTree').find("tbody").empty();
						for (var i = 0; i < flen; i++) {
							var temp_tr = document.createElement("tr");
							var temp_td1 = document.createElement("td");
							var temp_td2 = document.createElement("td");
							var temp_td3 = document.createElement("td");
							var temp_td4 = document.createElement("td");
							//var temp_a =document.createElement("a");
							//var temp_bt = document.createElement("button");

							//var temp_a = document.createElement("a");

							temp_td1.innerText = "文件";
							temp_td2.innerText = data.filename[i];
							if (data.resultfile[i]=="1"){
								temp_td4.innerText = "拥有权限";
							} else if(data.resultfile[i]=="0"){
								temp_td4.innerText = "无权限访问";
							}
							//alert("into this");
							//temp_a.appendChild(temp_bt);
							//temp_td4.appendChild(temp_a);
							temp_tr.appendChild(temp_td1);
							temp_tr.appendChild(temp_td2);
							temp_tr.appendChild(temp_td3);
							temp_tr.appendChild(temp_td4);
							$("#fileTree").find("tbody").append(temp_tr);
						}
						for (var i = 0; i < dlen; i++) {
							//alert("into dir");
							var atemp_tr = document.createElement("tr");
							var atemp_td1 = document.createElement("td");
							var atemp_td2 = document.createElement("td");
							var atemp_td3 = document.createElement("td");
							var atemp_td4 = document.createElement("td");
							//var temp_a = document.createElement("a");

							atemp_td1.innerText = "文件夹";
							atemp_td2.innerText = data.dirname[i];
							if (data.resultdir[i]=="1"){
								atemp_td4.innerText = "拥有权限";
							} else if(data.resultdir[i]=="0"){
								atemp_td4.innerText = "无权限访问";
							}
							atemp_tr.appendChild(atemp_td1);
							atemp_tr.appendChild(atemp_td2);
							atemp_tr.appendChild(atemp_td3);
							atemp_tr.appendChild(atemp_td4);
							$("#fileTree").find("tbody").append(atemp_tr);
						}
					}
				});
			}else{
				alert("这是文件");
			}
			}else{
				alert("无访问权限！");
			}

		});

		$("#parent").on("click",function() {
				$.ajax({
					type: 'GET',
					url: '/get_file_parent',
					data: {name: data},
					async: true,
					dataType: 'json',//希望服务器返回json格式的数据
					success: function (data) {
						//alert(data.filename.length);
						//alert(data.dirname.length);
						var flen = data.filename.length;
						var dlen = data.dirname.length;
						$('#fileTree').find("tbody").empty();
						for (var i = 0; i < flen; i++) {
							var temp_tr = document.createElement("tr");
							var temp_td1 = document.createElement("td");
							var temp_td2 = document.createElement("td");
							var temp_td3 = document.createElement("td");
							var temp_td4 = document.createElement("td");
							//var temp_a =document.createElement("a");
							//var temp_bt = document.createElement("button");

							//var temp_a = document.createElement("a");

							temp_td1.innerText = "文件";
							temp_td2.innerText = data.filename[i];
							if (data.resultfile[i]=="1"){
								temp_td4.innerText = "拥有权限";
							} else if(data.resultfile[i]=="0"){
								temp_td4.innerText = "无权限访问";
							}
							//temp_bt.type="button";
							//temp_bt.className="btn btn-default";
							//temp_bt.innerText="下载";
							//alert("into this");
							//temp_a.appendChild(temp_bt);
							//temp_td4.appendChild(temp_a);
							temp_tr.appendChild(temp_td1);
							temp_tr.appendChild(temp_td2);
							temp_tr.appendChild(temp_td3);
							temp_tr.appendChild(temp_td4);
							$("#fileTree").find("tbody").append(temp_tr);
						}
						for (var i = 0; i < dlen; i++) {
							//alert("into dir");
							var atemp_tr = document.createElement("tr");
							var atemp_td1 = document.createElement("td");
							var atemp_td2 = document.createElement("td");
							var atemp_td3 = document.createElement("td");
							var atemp_td4 = document.createElement("td");
							//var temp_a = document.createElement("a");
							if (data.resultdir[i]=="1"){
								atemp_td4.innerText = "拥有权限";
							} else if(data.resultdir[i]=="0"){
								atemp_td4.innerText = "无权限访问";
							}
							atemp_td1.innerText = "文件夹";
							atemp_td2.innerText = data.dirname[i];
							atemp_tr.appendChild(atemp_td1);
							atemp_tr.appendChild(atemp_td2);
							atemp_tr.appendChild(atemp_td3);
							atemp_tr.appendChild(atemp_td4);
							$("#fileTree").find("tbody").append(atemp_tr);
						}
					}
				});
		});

		$("#searchfile").on("click",function(){
			alert("into");
			var data=$("#filename").val();
			//alert(data);
		$.ajax({
        type:'get',
        url:'/search_file',
        data:{name:data},
		async:true,
        dataType:'json',//希望服务器返回json格式的数据
        success:function(data){
						//alert(data.filename.length);
						//alert(data.dirname.length);
						var flen = data.filename.length;
						var dlen = data.dirname.length;
						$('#fileTree').find("tbody").empty();
						for (var i = 0; i < flen; i++) {
							var temp_tr = document.createElement("tr");
							var temp_td1 = document.createElement("td");
							var temp_td2 = document.createElement("td");
							var temp_td3 = document.createElement("td");
							var temp_td4 = document.createElement("td");
							//var temp_a =document.createElement("a");
							//var temp_bt = document.createElement("button");

							//var temp_a = document.createElement("a");

							temp_td1.innerText = "文件";
							temp_td2.innerText = data.filename[i];
							if (data.resultfile[i]=="1"){
								temp_td4.innerText = "拥有权限";
							} else if(data.resultfile[i]=="0"){
								temp_td4.innerText = "无权限访问";
							}
							//temp_bt.type="button";
							//temp_bt.className="btn btn-default";
							//temp_bt.innerText="下载";
							//alert("into this");
							//temp_a.appendChild(temp_bt);
							//temp_td4.appendChild(temp_a);
							temp_tr.appendChild(temp_td1);
							temp_tr.appendChild(temp_td2);
							temp_tr.appendChild(temp_td3);
							temp_tr.appendChild(temp_td4);
							$("#fileTree").find("tbody").append(temp_tr);
						}
						for (var i = 0; i < dlen; i++) {
							//alert("into dir");
							var atemp_tr = document.createElement("tr");
							var atemp_td1 = document.createElement("td");
							var atemp_td2 = document.createElement("td");
							var atemp_td3 = document.createElement("td");
							var atemp_td4 = document.createElement("td");
							//var temp_a = document.createElement("a");
							if (data.resultdir[i]=="1"){
								atemp_td4.innerText = "拥有权限";
							} else if(data.resultdir[i]=="0"){
								atemp_td4.innerText = "无权限访问";
							}
							atemp_td1.innerText = "文件夹";
							atemp_td2.innerText = data.dirname[i];
							atemp_tr.appendChild(atemp_td1);
							atemp_tr.appendChild(atemp_td2);
							atemp_tr.appendChild(atemp_td3);
							atemp_tr.appendChild(atemp_td4);
							$("#fileTree").find("tbody").append(atemp_tr);
						}
		}
		});
		});

    });