export const SubmitValidate = (email, password)  => {
    return email.length > 0 && password.length > 0
}


export const RegisterValidate = (fname, lname, email, password) => {
    return fname.length > 0 && lname.length > 0 && email.length > 0 && password.length > 0;
}

export const MessageValidate = (message) => {
    return message.length > 0
}