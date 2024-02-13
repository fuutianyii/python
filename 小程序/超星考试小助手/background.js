// background.js

// 当插件图标被点击时触发
chrome.browserAction.onClicked.addListener(function(tab) {
    // 发送消息到当前活动标签页
    chrome.tabs.sendMessage(tab.id, {message: 'togglePlugin'});
});

// 监听来自内容脚本的消息
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    // 如果消息是来自内容脚本，并且是按下了 'a' 键或 'b' 键
    if (request.message === 'aPressed') {
        // 向当前标签页发送消息，调用页面 JavaScript 函数 getTheNextQuestion(1)
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.executeScript(
                tabs[0].id,
                {code: 'getTheNextQuestion(1);'}
            );
        });
    } else if (request.message === 'bPressed') {
        // 向当前标签页发送消息，调用页面 JavaScript 函数 getTheNextQuestion(-1)
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.executeScript(
                tabs[0].id,
                {code: 'getTheNextQuestion(-1);'}
            );
        });
    }
});
