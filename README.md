# Top-Kart_Nimish_Kalwar
API bundles for top kart in django


## Table of contents

* [General info](#general-info)
* [Methods and Tools](#methods-and-tools)
* [Status](#status)
* [Contact](#contact)

## General info

  Context:
  A global E-commerce website named Topkart uses an API to handle lightning deals. Lightning deals are products that are available at a discounted price on the website for a brief   amount of time. The expiry time of a lightning deal is not more than 12 hours. These will be refreshed at 00:00 UTC daily. The functionality of Topkart API:  

  Admin actions  
  Create and update lightning deals  
  Approve orders  

  Customer actions  
  Access available unexpired deals  
  Place orders  
  Check the status of their order  


  A lightning deal contains the following data points:  
  Product Name  
  Actual & Final price  
  Total & Available units  
  Expiry Time  

  Requirement:  
  Build an API to handle Topkart’s lightning deals.  

  Considerations:  
  Users should not be able to place an order for a deal that is expired  
  
  API's used by seller  
  1. to create deal  
      POST-/create-deal/    
      payload example:  
      {  
        "product_name":"test",  
        "actual_price":"10",  
       "discounted_price":"5",  
       "units":3  
        }  
   
  2. to update order  
     POST- /update-order/  
      payload example:  
      {  
        "product_name":"test"  
        }  
        
  API's used by customer  
  1. to fetch deals  
      GET- /fetch-deals/   
  
  2. to create order  
      POST- /create-order/  
      payload example:  
      {  
       "product_name":"test",  
        "price":"10",  
       "buyer_name":"abc",  
       "quantity":2  
        }  
  
  3. to track status
      POST- /track-status/  
      payload example:  
      {  
       "product_name":"test"   
        }  
        
 * To expire deal after 12 hours automatically, project is using jobs(apscheduler) which will run every 10 seconds to check if there is any deal which needs to expire


## Methods and Tools

* Python=3.7 
* Django=3.2
* apscheduler jobs


 
## Status
Project is: _finished_.

## Contact
If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on 
<a href="mailto:nimishkalwar1121@gmail.com">email</a> or 
<a href="https://www.linkedin.com/in/nimish-kalwar/" target="_blank">LinkedIn</a>
