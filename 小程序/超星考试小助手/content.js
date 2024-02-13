// content.js

// 监听键盘事件
document.addEventListener('keydown', function(event) {
    // 如果按下 'a' 键
    if (event.key === 'PageDown' || event.key ==='ArrowRight') {

        document.querySelector("#fanyaMarking > div.marking_content > div > div > div.nextDiv > a.jb_btn.jb_btn_92.fs14").click()

        
    }
    // 如果按下 'b' 键
    else if (event.key === 'PageUp' || event.key ==="ArrowLeft") {

        document.querySelector("#fanyaMarking > div.marking_content > div > div > div.nextDiv > a.btnBlue.btn_92.fs14").click()

    }
    else{function moveMouseTo(x, y) {
    var event = new MouseEvent('mousemove', {
        bubbles: true,
        cancelable: true,
        view: window,
        clientX: x,
        clientY: y
    });
    document.dispatchEvent(event);
}

// 调用 moveMouseTo 函数，并指定目标坐标
var targetX = 100; // 替换为您想要移动到的目标 x 坐标
var targetY = 100; // 替换为您想要移动到的目标 y 坐标
moveMouseTo(targetX, targetY);
}
});

// 监听来自 background.js 的消息
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    // 如果消息是切换插件状态
    if (request.message === 'togglePlugin') {
        // 执行相应的操作，例如显示/隐藏某些内容
    }
});
