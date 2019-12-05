import ipaddress
import re
import socket
##########################################  Normal Logic  ############################################################
class NormalLogic:
    def validateIPV4(self,address):
        arr = address.split('.')
        if(len(arr)==4):
            for i in range(0,len(arr)):
                if(len(arr[i])<=3):
                    try:
                        num = int(arr[i])
                    except:
                        return 0
                    if(0<=num and num<=255):
                        if('0' in arr[i] and arr[i].index('0')==0):
                            temp_i=arr[i].lstrip('0')
                            if(len(temp_i)==0 or int(temp_i)< 8):
                                pass
                            else:
                                return 0
                        # else:
                        #     pass
                    else:
                        return 0
                else:
                    return 0
            return 1
        else:
            return 0

    def validateIPV6(self,address):
        arr = address.split(':')
        if(len(arr)<8 and '' not in arr):
            return 0
        for i in arr:
            if(len(i)!=0):
                try:
                    num = int(i,16)
                except ValueError:
                    return 0
        return 1

    def IPAddressValidation(self,addresses):
        result = []
        for i in addresses:
            if('.' in i):
                if(self.validateIPV4(i.lower())):
                    result.append('IPv4')
                else:
                    result.append('Neither')
            elif(':' in i):
                if(self.validateIPV6(i.lower())):
                    result.append('IPv6')
                else:
                    result.append('Neither')
        return result
##########################################  Using socket module  #######################################################
class SocketMethod:
    def validateIPV4(self,address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:  # not a valid address
            return False
        return True

    def validateIPV6(self,address):
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except socket.error:  # not a valid address
            return False
        return True
    def IPAddressValidation(self,addresses):
        result = []
        for i in addresses:
            if('.' in i):
                if(self.validateIPV4(i.lower())):
                    result.append('IPv4')
                else:
                    result.append('Neither')
            elif(':' in i):
                if(self.validateIPV6(i.lower())):
                    result.append('IPv6')
                else:
                    result.append('Neither')
        return result
##########################################  Using ipaddress module  ####################################################
class IPAddressModule:
    def validateIPV4(self,str):
        try:
            addr = ipaddress.IPv4Address(str)
            return 1
        except ipaddress.AddressValueError:
            return 0
    def validateIPV6(self,str):
        try:
            addr = ipaddress.IPv6Address(str)
            return 1
        except ipaddress.AddressValueError:
            return 0
##########################################  Regex Logic 1  ############################################################
class RegexMethod1:
    def validateIPV4(self):
        byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'  # 0 - 255
        regex = '^{0}(\.{0}){{3}}$'.format(byte)
        pattern = re.compile(regex)
        return pattern
    def validateIPV6(self):
        hex_group = '[0-9A-Fa-f]{1,4}'  # Four hex digits
        regex = '^({0})(:{0}){{7}}$'.format(hex_group)
        pattern = re.compile(regex)
        return pattern
##########################################  Regex Logic 2  ############################################################
class RegexMethod2:
    def validateIPV6(self,str):
        if('::' in str):
            dum_str = ""
            arr = str.split(":")
            dum_arr = [string for string in arr if len(string) > 0]
            req_rep = 8-len(dum_arr)
            for i in arr:
                if(len(i)>0):
                    dum_str += i
                    dum_str += ":"
                else:
                    while(req_rep > 0):
                        dum_str += "0:"
                        req_rep -= 1
            str = dum_str.rstrip(":")
            #print(str)
        my_str=str.split(":")
        m=re.search(
            r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$',
            str)
        #print(m.groups())
        if(m):
            for i in my_str:
                if(0<= int(i,16) and int(i,16)<=65535):
                    pass
                else:
                    return 0
            return 1
        else:
            return 0
    def validateIPV4(self,str):
        m=re.search(r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', str)
        #print(m.groups())
        my_str = str.split(".")
        if(m):
            for i in my_str:
                if(0<= int(i,16) and int(i,16)<=255):
                    pass
                else:
                    return 0
            return 1
        else:
             return 0
##########################################  Final Solution  ############################################################
class FinalSolution:
    def IPAddressValidation(self,addresses):
        result = []
        ipv4_address = re.compile(
            '^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        ipv6_address = re.compile(
            '^(?:(?:[0-9A-Fa-f]{1,4}:){6}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::(?:[0-9A-Fa-f]{1,4}:){5}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){4}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){3}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,2}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){2}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,4}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(?:(?:[0-9A-Fa-f]{1,4}:){,6}[0-9A-Fa-f]{1,4})?::)$')
        for i in addresses:
            if ipv4_address.match(i):
                result.append('IPv4')
            elif ipv6_address.match(i):
                result.append('IPv6')
            else:
                result.append('Neither')
        return result

### Main Method ###
if __name__ == "__main__":
    str1 = ['121.18.19.20','0.12.12.34','121.234.12.12','23.45.12.56','0.1.2.3']
    str2 = ['2001:0db8:0000:0000:0000:ff00:0042:8329','2001:db8:0:0:0:ff00:42:8329','2001:db8::ff00:42:8329','0000:0000:0000:0000:0000:0000:0000:0001','::1']
    str3 = ['000.012.234.23','666.666.23.23','.213.123.23.32','23.45.22.32.','272:2624:235e:3bc2:c46d:682:5d46:638g','1:22:333:4444']
    print(FinalSolution().IPAddressValidation(str2))