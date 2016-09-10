#auther : pratik
# 006 PRODUCTS endpoint  Negative TC-1  empty payload

import DB_Connect
import Requrie
import json

#create a object of REQ() and DBConnect() class
rq = Requrie.REQ()
qry = DB_Connect.DBConnect()


def test_negative_TC1_product_empty_payload():
    print ("TC 1: Running Test case with Product endpoint with empty payload jason")

    input_data = {}
    info = rq.Post('products', input_data)
    print info

    response_code = info[0]
    print "Response code : ", response_code
    response_body = info[1]
    print json.dumps(response_body, indent=4)
    print "API URL : ", info[2]

    assert response_code == 400, "The response code is not expected. Expected: 400, Actual: {act}".format(act=response_code)
    assert 'errors' in response_body.keys(), "Response body doesn't contain errors"
    # response_body.keys() list all keys in error message ....here only one key is 'errors'

    exp_error_msg = "No product data specified to create product"
    Actual_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == Actual_error_msg, "No error message found"

    exp_error_code = "woocommerce_api_missing_product_data"
    Actual_error_code = response_body['errors'][0]['code']
    assert exp_error_code == Actual_error_code, "No error code found"


#007 PRODUCTS endpoint  Negative TC-2  missing title parameter

def test_negative_TC2_missing_title_parameter():
    print ("TC 2: Running Test case with Product having missing title parameter")

    title = 'Apple iPhone'
    price = '9.99'
    input_data = {
        "product": {
            #"title": title,
            "type": "simple",
            "regular_price": price,}}

    info = rq.Post('products', input_data)
    print info

    response_code = info[0]
    print "Response code : ", response_code
    response_body = info[1]
    print json.dumps(response_body, indent=4)
    print "API URL : ", info[2]

    assert response_code == 400, "The response code is not expected. Expected: 400, Actual: {act}".format(act=response_code)
    assert 'errors' in response_body.keys(), "Response body doesn't contain errors"
    # response_body.keys() list all keys in error message ....here only one key is 'errors'

    exp_error_msg = "Missing parameter title"
    Actual_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == Actual_error_msg, "No error message found"

    exp_error_code = "woocommerce_api_missing_product_title"
    Actual_error_code = response_body['errors'][0]['code']
    assert exp_error_code == Actual_error_code, "No error code found"


#test_negative_TC1_product_empty_payload()
test_negative_TC2_missing_title_parameter()