      alert("alert");
        $(function () {		// 标准写法，表示包含在function(){}之内的函数和变量都必须是在页面完全加载完毕后才发挥作用
            'use strict';	// 标准写法，JS的格式要求


            var url = '/sketch/upload';
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
