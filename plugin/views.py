from django.http import HttpResponse,JsonResponse
from Arifpay_Plugin import ArifPay
arifpay= ArifPay("G8FbER8zZ9uco5tLuVnNKycJwXzvJTyo","2025-02-01T03:45:27")
paymentInfo={
    "cancelUrl": "https://example.com",
    "errorUrl": "http://error.com",
    "notifyUrl": "https://gateway.arifpay.net/test/callback",
    "successUrl": "http://example.com",
    "paymentMethods": [
        "TELEBIRR"
    ],
    "expireDate": "2025-02-01T03:45:27",
    "items": [
        {
            "name": "ሙዝ",
            "quantity": 1,
            "price": 1,
            "description": "Fresh Corner preimuim Banana.",
            "image": "https://4.imimg.com/data4/KK/KK/GLADMIN-/product-8789_bananas_golden-500x500.jpg"
        },
        {
            "name": "ሙዝ",
            "quantity": 1,
            "price": 1,
            "description": "Fresh Corner preimuim Banana.",
            "image": "https://4.imimg.com/data4/KK/KK/GLADMIN-/product-8789_bananas_golden-500x500.jpg"
        }
    ],
    "beneficiaries": [
        {
            "accountNumber": "01320811436100",
            "bank": "AWINETAA",
            "amount": 2.0
        }
    ],
    "lang": "EN",
}
def createcheckout(request):
    if request.method=='GET':
        response=arifpay.Make_payment(paymentInfo)
        return JsonResponse(response)