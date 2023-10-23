# made by m1n007

from burp import IBurpExtender, IHttpListener

json_string = ''
hostTarget = ""
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
                if response_body.find(condition) != -1:
                    print(new_headers_response)
                    new_headers_response[0] = "HTTP/2 200 OK";
                    new_headers = new_headers_response;
                    print(new_headers)
                    new_message = self._helpers.buildHttpMessage(new_headers, self._helpers.stringToBytes(json_string))
                    content.setResponse(new_message)

        
        
         
