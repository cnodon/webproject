jwplayer("player").setup({
    "file": "/static/video/video1.mp4",
    "image": "/static/images/image1.jpg",
    "height": 360,
    "width": 640
})
jwplayer().on('complete',function() {
    alert("thanks for watching the video");
});
