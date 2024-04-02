$(document).ready(function(){

    frappe.call({
        method: "kartoza_shop.kartoza_shop.doctype.e_commerce_currency.e_commerce_currency.retrieve_currency_cache", //dotted path to server method
        type: "GET",
        callback: function(r) {
            // code snippet
            var currency = r.message
            try {
                document.getElementById("dropdownMenuButton").innerText = currency
            } catch (error) {
                
            }
        }
    });

    $('#currencyChange').change(function(){
        selected_value = $("input[name='currency']:checked").val();

        frappe.call({
            method: "kartoza_shop.kartoza_shop.doctype.e_commerce_currency.e_commerce_currency.set_currency_cache", //dotted path to server method
            type: "GET",
            args: {
                "currency": selected_value
            },
            callback: function(r) {
                // code snippet
                console.log(r.message)
                location.reload()
            }
        });
    });
});