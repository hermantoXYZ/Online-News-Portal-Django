document.addEventListener('DOMContentLoaded', function () {
    var images = document.querySelectorAll('img[data-ckimage="true"]');
    images.forEach(function (img) {
        var div = document.createElement('div');
        div.className = 'player-wrapper rounded overflow-hidden';
        img.parentNode.insertBefore(div, img);
        div.appendChild(img);
    });
});