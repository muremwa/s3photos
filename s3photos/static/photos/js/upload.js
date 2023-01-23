// display file to be uploaded
$(document).on('change', '#id_file', function (e) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $("#image-to-call").attr('src', e.target.result);
        $("#image-to-call").trigger('scrollIntoView', { block: "center", behavior: "smooth" });
    }
    reader.readAsDataURL(this.files[0])
    document.querySelector('.File-alert').style.display = 'none';
    document.querySelector('.img-to-up').style.display = 'block';
})