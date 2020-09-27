$(document).on('click', '.liking', function () {
    var img = this;
    var url = this.dataset["likeUrl"];
    var token = this.parentElement.children['csrfmiddlewaretoken'].value;
    var value = this.parentElement.children['count'];
    
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (response) {
            if (response['liked']) {
                img.src = '/static/svg/heart_full.svg';
            } else {
                img.src = '/static/svg/heart.svg';
            }
            value.innerText=response['likes'];            
        }
    });

});
