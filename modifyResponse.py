# made by m1n007

from burp import IBurpExtender, IHttpListener

json_string = '{ "meta": { "status": "200", "memoryusage": "1280240", "elapstime": 0.02780604362487793, "timestamp": 1697982497, "description": "Success" }, "data": { "email": "", "username": "nuggets070560", "device_id": "", "referral_code": "", "referral_count": 8, "max_referral": 8, "virtual_store": "https://api-mgm-indo.antikode.dev/assets/img/store/0.png", "xp": 50, "rank": { "period": 1642, "all_time": 1641 }, "referral_stage": [ { "count": 1, "status": true, "referral_reward": null }, { "count": 2, "status": true, "referral_reward": null }, { "count": 3, "status": true, "referral_reward": { "name": "Reward Pertama", "reward": { "title": "Main Reward 3/8", "description": "Nikmati 1 Ayam Krispy McD + 1 Nasi Reguler + 1 Lemon Tea Reguler cuma Rp 18.182", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/reward/pbEMionxpw.png", "reward_member": { "is_claimed": 1 } } } }, { "count": 4, "status": true, "referral_reward": null }, { "count": 5, "status": true, "referral_reward": null }, { "count": 6, "status": true, "referral_reward": null }, { "count": 7, "status": true, "referral_reward": null }, { "count": 8, "status": true, "referral_reward": { "name": "REWARD UTAMA", "reward": { "title": "Main Reward 8/8", "description": "Nikmati 2 Ayam Krispy McD + 1 Nasi Reguler + 1 Lemon Tea Reguler cuma Rp 27.273", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/reward/L669yoVBNH.png", "reward_member": { "is_claimed": 1 } } } } ], "quest": { "status": true, "list": [ { "uuid": "e84781bb-6ad4-4132-94b9-8a3a361b9093", "name": "Tukarkan 20 Poin MyM Rewards", "description": "Dapatkan 50XP dan 1 Ayam Krispy McD + Regular Fries dengan harga spesial Rp 9.091", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/quest/l43ytf7JZ3.png", "points": 0, "xp": 0, "claimed": false, "reward": { "title": "Extra Mission 1", "description": "Beli 1 Ayam Krispy McD + 1 Regular Fries cuma Rp 9.091", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/reward/Dzl5FxJw11.png", "offer_id": "149773", "loyalty_id": "3871" } }, { "uuid": "8414c52c-f24d-417f-9d55-6c8f0a5a0f40", "name": "Tukarkan 20 Poin MyM Rewards", "description": "Dapatkan 50XP dan 1 Ayam Krispy McD + Cheeseburger dengan harga spesial Rp 9.091", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/quest/O0kIsMRRqy.png", "points": 0, "xp": 0, "claimed": false, "reward": { "title": "Extra Mission 2", "description": "Beli 1 Ayam Krispy McD + 1 Cheeseburger cuma Rp 9.091", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/reward/tXNL0uKrJ3.png", "offer_id": "149775", "loyalty_id": "3871" } }, { "uuid": "44967942-1302-4522-b3cc-350f5cc7208f", "name": "Tukarkan 20 Poin MyM Rewards", "description": "Dapatkan 50XP dan 2 Ayam Krispy McD + Medium Lemon Tea dengan harga spesial Rp 13.636", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/quest/pxwjWQSRbj.png", "points": 0, "xp": 0, "claimed": false, "reward": { "title": "Extra Mission 3", "description": "Beli 2 Ayam Krispy McD + 1 Lemon Tea Medium cuma Rp 13.636", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/reward/5JBWe1dqta.png", "offer_id": "149776", "loyalty_id": "3871" } }, { "uuid": "97695e9f-1115-48a7-a16c-722d7e495fef", "name": "Tukarkan 20 Poin MyM Rewards", "description": "Dapatkan 50XP dan 1 Ayam Krispy McD + 1 Ayam Spicy McD + McFlurry feat. Oreo dengan harga spesial Rp 13.636", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/quest/fnMOzwaOXj.png", "points": 0, "xp": 0, "claimed": false, "reward": { "title": "Extra Mission 4", "description": "Beli 1 Ayam Spicy McD + 1 Ayam Krispy McD + 1 McFlurry feat. Oreo cuma Rp 13.636", "image": "https://mcdonalds-mgm-indo.s3.ap-southeast-3.amazonaws.com/storage/mgm/reward/LEfDLeLsuh.png", "offer_id": "149778", "loyalty_id": "3871" } } ] }, "reward_welcome": null } }'
hostTarget = "api-mgm-indo.mcdonalds.co.id"
condition = "Device id not match"
        

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        extName = "Auto Modify Object Response"
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        callbacks.registerHttpListener(self)
        callbacks.setExtensionName(extName)

        return

    def getResponseHeadersAndBody(self, content):
        request = content.getRequest()
        request_data = self._helpers.analyzeResponse(request)
        request_headers = list(request_data.getHeaders() or '')
        
        response = content.getResponse()
        response_data = self._helpers.analyzeResponse(response)
        headers = list(response_data.getHeaders() or '')
        body = response[response_data.getBodyOffset():].tostring()
        return headers, body, request_headers

    def processHttpMessage(self, tool, isRequest, content):
        if isRequest:
            return
        
        print('Waiting host :', hostTarget)
        new_headers_response, response_body, request_headers = self.getResponseHeadersAndBody(content);
        if any(hostTarget in header for header in request_headers):
            print('Host Found!')
            
            if any("4" in header for header in new_headers_response):
                print(new_headers_response)
                new_headers_response[0] = "HTTP/2 200 OK";
                new_headers = new_headers_response;
                print(new_headers)
                new_message = self._helpers.buildHttpMessage(new_headers, self._helpers.stringToBytes(json_string))
                content.setResponse(new_message)

        
        
         
