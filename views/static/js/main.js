console.log("%cCopyright © "+ new Date().getFullYear() +"%c短网址生成器 by 相左",
    "color:white;background:#313a46;padding:3px 7px;border-top-left-radius: 3px;border-bottom-left-radius: 3px;",
    "color:white;background:#727cf5;padding:3px 7px;border-top-right-radius: 3px;border-bottom-right-radius: 3px;"
)

$(document).ready(function(){
    $("#submit").click(function(){
    var longUrl = $(".post-input").val()
    if(longUrl){
        $.ajax({
        url: "/api",
        type: "get",
        data: {
            "url": longUrl
        },
        success: ((res)=>{
            if(res.code == 200){
                shortUrl = res.data.shortUrl
                $("#shortUrl").text(shortUrl)
                Qmsg.success("短网址生成成功！")
            }else{
                Qmsg.warning(res.msg)
            }
        }),
        error: ((res)=>{
            Qmsg.error("短网址生成失败！")
        })
        })
    }else{
        Qmsg.warning("请输入长链接再提交！")
    }
    })

    $("#goUrl").click(function(){
        var shortUrl = $("#shortUrl").text()
        if(shortUrl == window.location.href){
            Qmsg.warning("没有要跳转的短链接!")
        }else{
            window.open(shortUrl)
        }
    })

    $("#copyUrl").click(function(){
        var shortUrl = $("#shortUrl").text()
        if(shortUrl == window.location.href){
            Qmsg.warning("没有要复制的短链接!")
        }else{
            $('#copy').text(shortUrl).show();
            $('#copy').select();
            document.execCommand('copy', false, null);
            $('#copy').hide();
            Qmsg.success('复制成功!');
        }
    })
})