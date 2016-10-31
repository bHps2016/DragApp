$(function(){
    //阻止浏览器默认行。
    $(document).on({
        dragleave:function(e){    //拖离
            e.preventDefault();
        },
        drop:function(e){  //拖后放
            e.preventDefault();
        },
        dragenter:function(e){    //拖进
            e.preventDefault();
        },
        dragover:function(e){    //拖来拖去
            e.preventDefault();
        }
    });
    var target_qiniu;
    var target_foregin;
    var url = 'http://127.0.0.1:5000/upload/';
    var qiniu = document.getElementById("qiniu");
    var foregin = document.getElementById("foregin");
    var res_url_cont = document.getElementById("res_url_cont");
    var img_url = document.getElementById("img_url");
    var md_url = document.getElementById("md_url");
    var box = document.getElementById('file_box'); //拖拽区域
    qiniu.addEventListener("click", function(e){
        url = 'http://127.0.0.1:5000/oupload/';
        qiniu.className="nav_item qiniu flag";
        foregin.className="nav_item foregin";
    },false)
    foregin.addEventListener("click", function(e){
        url = 'http://127.0.0.1:5000/upload/';
        foregin.className="nav_item foregin flag";
        qiniu.className="nav_item qiniu";
    },false)
    res_url_cont.addEventListener("click", function(e){
        var target = e.target;
        var aux = document.createElement("input");

          // 获取复制内容
          var content = target.innerHTML || target.value;

          // 设置元素内容
          aux.setAttribute("value", content);

          // 将元素插入页面进行调用
          document.body.appendChild(aux);
          // 复制内容
          aux.select();

          // 将内容复制到剪贴板
          document.execCommand("copy");

          // 删除创建元素
          document.body.removeChild(aux);
    } , false)
    box.addEventListener("drop",function(e){
        e.preventDefault(); //取消默认浏览器拖拽效果
        var fileList = e.dataTransfer.files; //获取文件对象
        //检测是否是拖拽文件到页面的操作
        if(fileList.length == 0){
            return false;
        }
        //检测文件是不是图片
        if(fileList[0].type.indexOf('image')!==-1){
            //拖拉图片到浏览器，可以实现预览功能
            var img = window.URL.createObjectURL(fileList[0]);
            var filename = fileList[0].name; //图片名称
            var filesize = Math.floor((fileList[0].size)/1024);
            var str = "<img src='"+img+"'><p>图片名称："+filename+"</p><p>大小："+filesize+"KB</p>";
            $("#preview").html(str);
        }

        //上传
        xhr = new XMLHttpRequest();
        xhr.open("post", url , true);
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xhr.onload = function (res,err) {
          var res_url = JSON.parse(res.currentTarget.response).url;
          // var res_url = ''
          str = "外链（点击复制）：<div class='url_cont' id='url'>"+res_url+"</div>";
          str+= "<div class='url_cont' id='img_url'>&lt;img src='"+res_url+"&gt</div>";
          str+= "<div class='url_cont' id='md_url'>![]("+res_url+")</div>"
          $("#res_url_cont").html(str);
        };
        var fd = new FormData();
        fd.append('mypic', fileList[0]);

        xhr.send(fd);
    },false);
});
