function loginUser() {
    const Url = 'http://127.0.0.1:8000/auth/login'
    let Data = {
        "email" : $('#login-username').val,
        "password" : $('#login-password').val
    }
    let otherParams = {
        headers: {'content-type': 'application/json; charset=UTF-8'},
        body: JSON.stringify(Data),
        method: 'POST'
    }
    $.get(Url, otherParams).then(res => {
        console.log(res)
    });
}

function registerUser() {
    const Url = 'http://127.0.0.1:8000/auth/register'
    let Data = {
        email: $('#register-email').val,
        username: $('#register-username').val,
        password: $('#register-password').val,
        password2: $('#register-password2').val
    }
    let otherParam = {
        headers: {'content-type': 'application/json; charset=UTF-8'},
        body: JSON.stringify(Data),
        method: 'POST'
    }
    fetch(Url, otherParam).then(res => {
        console.log(res)
    });
}