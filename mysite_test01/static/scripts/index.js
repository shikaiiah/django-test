$(document).ready(function () {
    // 登录按钮
    $("#signin").click(function () {
        $("#login").show()
    });
    // 登录对话框关闭按钮
    $("#login-close").click(function () {
        $("#login").hide()
    });
});