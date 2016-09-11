# PRODUCTS endpoint  Negative TC-1 with empty payload

import DB_Connect
import Requrie
import json

# Create a object of REQ() and DBConnect() class

rq = Requrie.REQ()
qry = DB_Connect.DBConnect()


def test_negative_TC1_product_empty_payload():
    print ("TC 1: Running Test case with Product endpoint with empty payload jason")
    test_case = "TC 1"
    input_data = {}
    response_list = rq.Post('products', input_data)
    #print response_list

    response_code = response_list[0]
    print "Response code : ", response_code
    response_body = response_list[1]
    print json.dumps(response_body, indent=4)
    print "API URL : ", response_list[2]

    exp_error_msg = "No product data specified to create product"
    exp_error_code = "woocommerce_api_missing_product_data"
    verify_ng_test_response(response_list, test_case, exp_error_msg, exp_error_code)


    '''
    assert response_code == 400, "The response code is not expected. Expected: 400, Actual: {act}".format(act=response_code)
    assert 'errors' in response_body.keys(), "Response body doesn't contain errors"
    # response_body.keys() list all keys in error message ....here only one key is 'errors'

    exp_error_msg = "No product data specified to create product"
    Actual_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == Actual_error_msg, "No error message found"

    exp_error_code = "woocommerce_api_missing_product_data"
    Actual_error_code = response_body['errors'][0]['code']
    assert exp_error_code == Actual_error_code, "No error code found"

    '''
# PRODUCTS endpoint  Negative TC-2  with missing title parameter

def test_negative_TC2_missing_title_parameter():
    print ("TC 2: Running Test case with Product having missing title parameter")
    test_case = "TC 2"
    title = 'Apple iPhone'
    price = '9.99'
    input_data = {
        "product": {
            #"title": title,
            "type": "simple",
            "regular_price": price,}}

    response_list = rq.Post('products', input_data)
    #print response_list

    response_code = response_list[0]
    print "Response code : ", response_code
    response_body = response_list[1]
    print json.dumps(response_body, indent=4)
    print "API URL : ", response_list[2]

    exp_error_msg = "Missing parameter title"
    exp_error_code = "woocommerce_api_missing_product_title"
    verify_ng_test_response(response_list, test_case, exp_error_msg, exp_error_code)
    '''
    assert response_code == 400, "The response code is not expected. Expected: 400, Actual: {act}".format(act=response_code)
    assert 'errors' in response_body.keys(), "Response body doesn't contain errors"
    # response_body.keys() list all keys in error message ....here only one key is 'errors'

    exp_error_msg = "Missing parameter title"
    Actual_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == Actual_error_msg, "No error message found"

    exp_error_code = "woocommerce_api_missing_product_title"
    Actual_error_code = response_body['errors'][0]['code']
    assert exp_error_code == Actual_error_code, "No error code found"
    '''


def verify_ng_test_response(response_list, test_case, exp_error_msg, exp_error_code):

    # Verify response code
    response_code = response_list[0]
    assert response_code == 400, "The response code is for {tc} not expected. Expected: 400, Actual: {act}".format(tc=test_case,
        act=response_code)

    # Verify there is a key "error' in the response
    response_body = response_list[1]
    assert 'errors' in response_body.keys(), "For testcase {tc}, Response body doesn't contain errors".format(tc=test_case)

    # Verify content of error message
    Actual_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == Actual_error_msg, "Test Case {tc} is failed as actual message is : {actual} and expeted message is : " \
                                              "{exp},".format(tc=test_case, actual= Actual_error_msg, exp= exp_error_msg)


    #Vetify error code in response
    Actual_error_code = response_body['errors'][0]['code']
    assert exp_error_code == Actual_error_code, "Test Case {tc} is failed as actual message is : {actual} and expeted message is : " \
                                              "{exp},".format(tc=test_case, actual=Actual_error_code, exp=exp_error_code)



test_negative_TC1_product_empty_payload()
print "================================================================="
test_negative_TC2_missing_title_parameter()
