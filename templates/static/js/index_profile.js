/**
* Template Name: eCommece - v0.0.1
* Author: agnsuporte
*/

const btnRegister = document.getElementById("btn-register");
const btnLogin = document.getElementById("btn-login");
const divRegister = document.getElementById("div-register");
const divLogin = document.getElementById("div-login");
const noMember = document.getElementById("notMember");

const onBtnRegisterClick = (e) => {
    e.preventDefault();
    btnRegister.classList.add("active");
    btnLogin.classList.remove("active");
    divRegister.classList.add("show", "active");
    divLogin.classList.remove("show", "active");
};

const onBtnLoginClick = (e) => {
    e.preventDefault();
    btnRegister.classList.remove("active");
    btnLogin.classList.add("active");
    divRegister.classList.remove("show", "active");
    divLogin.classList.add("show", "active");
};

btnRegister.addEventListener("click", onBtnRegisterClick);
noMember.addEventListener("click", onBtnRegisterClick);
btnLogin.addEventListener("click", onBtnLoginClick);