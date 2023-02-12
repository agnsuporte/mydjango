/**
* Template Name: eCommece - v0.0.1
* Author: agnsuporte
*/
document.addEventListener('DOMContentLoaded', () => {
  "use strict";

  /**
   * Select Variation
   */
  const elSelectVariations = document.getElementById("select-variacoes");
  if (elSelectVariations) {
    elSelectVariations.addEventListener("change", function () {
      const selectedOption = this.options[this.selectedIndex];
      const valueProduct = selectedOption.dataset.priceProduct;
      const valueProductPromotional = selectedOption.dataset.pricePromotional;
      const elPriceProduct = document.getElementById("price-product");
      const elPricePromotional = document.getElementById("price-promotional");
      if (parseFloat(valueProductPromotional) <= 0) {
        if (elPriceProduct.classList.contains('text-decoration-line-through')) {
          elPriceProduct.classList.remove('text-decoration-line-through')
        }
        elPricePromotional.innerHTML = '';
        elPricePromotional.style.display = 'none';
      } else {
        if (!elPriceProduct.classList.contains('text-decoration-line-through')) {
          elPriceProduct.classList.add('text-decoration-line-through')
        }
        elPricePromotional.style.display = 'block';
        elPricePromotional.innerHTML = '<i class="bi bi-currency-euro"></i>' + valueProductPromotional;
      }
      elPriceProduct.innerHTML = valueProduct;
      document.getElementById("product-name").innerHTML = selectedOption.text;
    });
  }
  
});