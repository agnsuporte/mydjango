/**
* PHP Email Form Validation - v3.5
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
    "use strict";

    let forms = document.querySelectorAll('#__form-add-to-cart');

    forms.forEach(function (e) {
        e.addEventListener('submit', function (event) {
            event.preventDefault();

            let thisForm = this;

            let action = thisForm.getAttribute('action');
            let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');

            if (!action) {
                displayError(thisForm, 'The form action property is not set!')
                return;
            }

            let formData = thisForm;
            let obj = {};
            for (let [key, value] of Object.entries(obj)) {
                obj[key] = value;
            }
            php_email_form_submit(action, obj);
        });
    });

    function php_email_form_submit(action, formData) {
        fetch(action, {
            method: 'POST',
            body: formData,
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
            .then(response => {
                return response.text();
            })
            .then(data => {
                console.log(data)
            })
            .catch((error) => {
                console.log('Deu merda!')
            });
    }

    function displayError(thisForm, error) {
        thisForm.querySelector('.loading').classList.remove('d-block');
        thisForm.querySelector('.error-message').innerHTML = error;
        thisForm.querySelector('.error-message').classList.add('d-block');
    }

})();