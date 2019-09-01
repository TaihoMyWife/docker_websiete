$(function () {		// 标准写法，表示包含在function(){}之内的函数和变量都必须是在页面完全加载完毕后才发挥作用
            'use strict';	// 标准写法，JS的格式要求


            var url = '/sketch/upload';
	    // ** 自定义一个新的url，我们假设有一个潜藏的页面叫作‘http://127.0.0.1:5000/sketch/upload’
	    // ** 我们希望在那个虚拟的地方进行与后台的数据交换，
	    // ** 因此，我们后台的对应函数的路由应该设置为“ @app.route('/sketch/upload') ”

	    // ** 下面我们打算构建一组东西，是给file按钮准备的，
	    // *  包括了：fileupload，prop，
	    // *  第一部分的fileupload包括了：url, 信息交互的数据类型，done，progressall
            $('#fileupload').fileupload({
                url: url,
                dataType: 'json',// 数据交互的类型

		// done表示当接收到后端反馈的信息是要做的动作
                done: function (e, data) {
                    var filepath = "", filepath_ = "";
                    $.each(data.result.files, function (index, file) {
                        $('<p style="display: none"/>').text(file.name).appendTo(document.body);
                        filepath = file.filepath;
                        filepath_ = file.filepath_;
                        document.getElementById('temp').value = filepath + "&" + filepath_;
                    });
                    $('#left').attr('src', '{{ url_for('static', filename='images/ue.png') }}');

                },// 这一部分小编会结合后端的函数一起讲解

		// progressall表示在选择好文件后上传文件过程中要做的动作
                progressall: function (e, data) {
		    // 显然这是对进度条做宽度变化
                    var progress = parseInt(data.loaded / data.total * 100, 10);
                    $('#progress .progress-bar').css(
                        'width',
                        progress + '%'
                    );
                }
            }).prop('disabled', !$.support.fileInput)
                .parent().addClass($.support.fileInput ? undefined : 'disabled');

        });

     $('#submit').on("click", function () {
    $('#progress .progress-bar').css(
        'width',
        0 + '%'
    );// 进度条重新归0
    $('#left').attr('src', '{{ url_for('static', filename='images/ul.png') }}');
    var filepath_ = document.getElementById('temp').value;// 获取刚刚存储在temp（text）上的数值

    // try to delete the original images
    var data = {
        'path': filepath_.split("&")[0],
        'path_': filepath_.split("&")[1]
    }// 对字符串做分割，并通过建立字典data进行分装
    $.ajax({
        type: 'GET',
        url:'/sketch/delete',// 标签的绑定
        data: data,                  
        dataType: 'json',             // 数据格式
        success: function(data){      
            
        }
    });
});
