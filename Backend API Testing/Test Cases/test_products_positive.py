# 002 PRODUCTS endpoint  Positive TC-1  create payload  make api call
# 003 PRODUCTS endpoint  Positive TC-1  verify the response
# 005 PRODUCTS endpoint  Positive TC-1  verify info in the DB

import DB_Connect
import Requrie
import json

#create a object of REQ() and DBConnect() class
rq = Requrie.REQ()
qry = DB_Connect.DBConnect()


# method for creating a product
def test_create_a_product():

    # create payload  make api call
    global rs_id
    global title
    global price

    title = 'Apple iPhone'
    price = '9.99'
    input_data = {
            "product": {
                "title": title,
                "type": "simple",
                "regular_price": price,}}

    info = rq.Post('Products',input_data)
    response_code = info[0]
    print "Response code : ", response_code
    response_body = info[1]
    print json.dumps(response_body, indent=4)
    print "API URL : ",info[2]

    # verify the response

    rs_title = response_body["product"]["title"]
    rs_price = response_body["product"]["regular_price"]
    rs_id = response_body["product"]["id"]

    assert response_code==201,"The response code is not expected. Expected: 201, Actual: {act}".format(act=response_code)
    assert rs_title == title, "The title name is not what we send in request. Actual: {}".format(rs_title)
    assert rs_price == price, "The price is not what we send in request. Expected: {},Actual: {}".format(price,rs_price)

    print "Product ID is :",rs_id
    print "create product test PASS"

    # Verify in DB

def test_verify_in_DB():
    sql='''select p.post_title, p.post_type, pm.meta_value from ak_posts p join ak_postmeta pm on p.id=pm.post_id where p.id={} and pm.meta_key='_regular_price' '''.format(rs_id)
    qrs = qry.SELECT('wp37', sql)
    print "=============================================="
    print qrs

    db_title = qrs[0][0]
    db_type =  qrs[0][1]
    db_regular_prize = qrs[0][2]

    assert db_title==title,"The title entryt in db is not currect"
    assert db_type == 'product', "The product entryt in db is not currect"
    assert db_regular_prize == price, "The price entryt in db is not currect"
    print "DB Verification is successful"
test_create_a_product()
test_verify_in_DB()