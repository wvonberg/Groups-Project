var orgName=""

$('#orgName').keydown(function(e){
    console.log('input was changed')
    console.log(e.target.value)
    orgName=e.target.value
    if (orgName.length < 5){
        document.getElementById('orgName').style.backgroundColor="#D59081"
    } else {
        document.getElementById('orgName').style.backgroundColor="#5BBF78"
    }

})


$('#createOrg').submit(function(e){
    e.preventDefault();
    console.log(e);
    console.log(this)
    if (orgName.length <5){
        alert('Org name must be longer than 5 characters')
        return null
    }
    $.ajax({
        url:'/create_org',
        method:"post",
        data: $(this).serialize(),
        success: function(serverResponse){
            console.log("This is Ajax working!")
            console.log(serverResponse)
            $('#groups').append(serverResponse);
        }
    })
    $(this).trigger('reset');
})
